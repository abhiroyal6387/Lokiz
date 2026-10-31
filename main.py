import json
import os
from threading import Thread

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window

from core.assistant import Assistant
from storage.database import Database
from voice.speech_output import speak
from voice.speech_input import listen


KV = """
<ChatBubble@Label>:
    size_hint_y: None
    text_size: self.width - dp(20), None
    height: self.texture_size[1] + dp(20)
    padding: dp(10), dp(8)
    markup: True
    halign: "left"
    valign: "middle"
    color: 0.94, 0.96, 1, 1

BoxLayout:
    orientation: "vertical"
    padding: "10dp"
    spacing: "6dp"
    canvas.before:
        Color:
            rgba: 0.03, 0.04, 0.09, 1
        Rectangle:
            pos: self.pos
            size: self.size

    # Header
    BoxLayout:
        size_hint_y: None
        height: "56dp"
        spacing: "6dp"
        Label:
            text: "[b]AMIE AI[/b]\\n[color=55ddf5]Your Personal AI Assistant[/color]"
            markup: True
            halign: "left"
            valign: "middle"
            text_size: self.size
            color: 1, 1, 1, 1
        Button:
            text: "⚙"
            size_hint_x: None
            width: "48dp"
            background_color: 0.15, 0.25, 0.45, 1
            on_release: app.open_settings()

    # Status bar
    Label:
        id: status_label
        text: app.status
        size_hint_y: None
        height: "26dp"
        color: 0.4, 0.85, 1, 1
        font_size: "13sp"

    # Chat area
    ScrollView:
        id: scroll
        do_scroll_x: False
        GridLayout:
            id: chat
            cols: 1
            spacing: "8dp"
            size_hint_y: None
            height: self.minimum_height
            padding: "4dp"

    # Input row
    BoxLayout:
        size_hint_y: None
        height: "52dp"
        spacing: "6dp"
        TextInput:
            id: msg
            hint_text: "Message Amie... (Hindi / English / Hinglish)"
            multiline: False
            background_color: 0.08, 0.1, 0.16, 1
            foreground_color: 0.95, 0.97, 1, 1
            cursor_color: 0.3, 0.8, 1, 1
            padding: "10dp", "12dp"
            on_text_validate: app.send()
        Button:
            text: "🎤"
            size_hint_x: None
            width: "48dp"
            background_color: 0.2, 0.15, 0.4, 1
            on_release: app.mic_pressed()
        Button:
            text: "SEND"
            size_hint_x: None
            width: "72dp"
            background_color: 0.1, 0.45, 0.75, 1
            on_release: app.send()

    # Bottom actions
    BoxLayout:
        size_hint_y: None
        height: "42dp"
        spacing: "8dp"
        Button:
            text: "Clear Chat"
            background_color: 0.35, 0.15, 0.2, 1
            on_release: app.confirm_clear()
        Button:
            text: "Speak Last"
            background_color: 0.15, 0.3, 0.35, 1
            on_release: app.speak_last()
"""


class AmieApp(App):
    status = StringProperty("Ready • API key required")
    busy = BooleanProperty(False)

    def build(self):
        self.title = "Amie AI"
        self.cfg = self._load_config()
        self.db = Database(self.user_data_dir)
        self.ai = Assistant(self.cfg, self.db)
        self.last_reply = ""
        self.root = Builder.load_string(KV)
        Clock.schedule_once(self._load_history, 0.3)
        Window.bind(on_keyboard=self._on_keyboard)
        return self.root

    # ---------- Config persistence ----------
    def _config_path(self):
        return os.path.join(self.user_data_dir, "config.json")

    def _load_config(self):
        path = self._config_path()
        default = {"api_key": "", "model": "gemini-2.5-flash"}
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                default.update(data)
            except Exception:
                pass
        return default

    def _save_config(self):
        try:
            with open(self._config_path(), "w", encoding="utf-8") as f:
                json.dump(self.cfg, f, indent=2)
        except Exception:
            pass

    # ---------- Chat UI ----------
    def _load_history(self, *args):
        for role, msg in self.db.latest(40):
            who = "YOU" if role == "user" else "AMIE"
            self.add_bubble(who, msg)
        self._scroll_to_bottom()

    def add_bubble(self, who, text):
        color = "55ddf5" if who == "AMIE" else "a0a8c0"
        label = Label(
            text=f"[b][color={color}]{who}[/color][/b]\n{text}",
            markup=True,
            size_hint_y=None,
            text_size=(Window.width - 40, None),
            halign="left",
            valign="middle",
            padding=(10, 8),
            color=(0.94, 0.96, 1, 1),
        )
        label.bind(
            texture_size=lambda inst, val: setattr(inst, "height", val[1] + 18)
        )
        label.height = 50
        self.root.ids.chat.add_widget(label)
        self._scroll_to_bottom()

    def _scroll_to_bottom(self):
        def _do(*a):
            scroll = self.root.ids.scroll
            scroll.scroll_y = 0
        Clock.schedule_once(_do, 0.05)

    # ---------- Send / Ask ----------
    def send(self):
        if self.busy:
            return
        text = self.root.ids.msg.text.strip()
        if not text:
            return
        self.root.ids.msg.text = ""
        self.add_bubble("YOU", text)
        self.db.add("user", text)
        self.busy = True
        self.status = "Thinking..."
        Thread(target=self._ask_thread, args=(text,), daemon=True).start()

    def _ask_thread(self, prompt):
        try:
            reply = self.ai.ask(prompt)
            err = False
        except Exception as e:
            reply = str(e) or "Request failed. Check API key, model, internet or quota."
            err = True
        Clock.schedule_once(lambda dt: self._finish(reply, err), 0)

    def _finish(self, reply, err):
        self.add_bubble("AMIE", reply)
        self.db.add("assistant", reply)
        self.last_reply = reply
        self.busy = False
        self.status = "Needs attention" if err else "Ready"
        # Optional auto-speak (can be noisy, so only on demand for now)

    # ---------- Settings ----------
    def open_settings(self):
        layout = BoxLayout(orientation="vertical", padding=12, spacing=8)
        layout.add_widget(Label(
            text="Paste your Gemini API key below.\nNever put the key in GitHub.",
            size_hint_y=None, height=50, color=(0.9, 0.9, 1, 1)
        ))
        key_input = TextInput(
            password=True, multiline=False,
            text=self.cfg.get("api_key", ""),
            hint_text="Gemini API key",
            size_hint_y=None, height=44
        )
        model_input = TextInput(
            multiline=False,
            text=self.cfg.get("model", "gemini-2.5-flash"),
            hint_text="Model ID (e.g. gemini-2.5-flash)",
            size_hint_y=None, height=44
        )
        layout.add_widget(Label(text="API Key", size_hint_y=None, height=22))
        layout.add_widget(key_input)
        layout.add_widget(Label(text="Model ID", size_hint_y=None, height=22))
        layout.add_widget(model_input)

        save_btn = Button(text="Save", size_hint_y=None, height=46,
                          background_color=(0.1, 0.5, 0.7, 1))
        layout.add_widget(save_btn)

        popup = Popup(title="Amie Settings", content=layout,
                      size_hint=(0.92, 0.55), auto_dismiss=True)

        def on_save(*args):
            self.cfg["api_key"] = key_input.text.strip()
            self.cfg["model"] = model_input.text.strip() or "gemini-2.5-flash"
            self._save_config()
            self.ai = Assistant(self.cfg, self.db)
            if self.cfg["api_key"]:
                self.status = "API key saved • Ready"
            else:
                self.status = "API key required"
            popup.dismiss()

        save_btn.bind(on_release=on_save)
        popup.open()

    # ---------- Clear chat ----------
    def confirm_clear(self):
        layout = BoxLayout(orientation="vertical", padding=12, spacing=10)
        layout.add_widget(Label(text="Delete all saved chat history?", size_hint_y=None, height=40))
        btn_row = BoxLayout(size_hint_y=None, height=46, spacing=8)
        yes = Button(text="Delete", background_color=(0.7, 0.2, 0.2, 1))
        no = Button(text="Cancel")
        btn_row.add_widget(yes)
        btn_row.add_widget(no)
        layout.add_widget(btn_row)
        popup = Popup(title="Confirm", content=layout, size_hint=(0.85, 0.3))

        def do_clear(*a):
            self.db.clear()
            self.root.ids.chat.clear_widgets()
            self.last_reply = ""
            popup.dismiss()
            self.status = "Chat cleared"

        yes.bind(on_release=do_clear)
        no.bind(on_release=popup.dismiss)
        popup.open()

    # ---------- Voice ----------
    def mic_pressed(self):
        if self.busy:
            return
        self.status = "Speech recognition not ready yet"
        try:
            text = listen()
            if text:
                self.root.ids.msg.text = text
                self.send()
        except NotImplementedError as e:
            self.status = str(e)
        except Exception as e:
            self.status = f"Mic error: {e}"

    def speak_last(self):
        if self.last_reply:
            speak(self.last_reply)
            self.status = "Speaking..."
        else:
            self.status = "No reply to speak"

    # ---------- Android back button ----------
    def _on_keyboard(self, window, key, *args):
        if key == 27:  # Escape / Android back
            self.stop()
            return True
        return False

    def on_pause(self):
        return True  # Allow Android to pause the app

    def on_resume(self):
        pass


if __name__ == "__main__":
    AmieApp().run()
