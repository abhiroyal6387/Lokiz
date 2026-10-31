# Amie AI — Fixed Starter (Kivy + Gemini + Buildozer)

Personal AI assistant for Android built with **Python + Kivy**.

## What is fixed / improved

- More complete and safer `buildozer.spec` (API 33, proper requirements, permissions)
- Reliable GitHub Actions workflow (Ubuntu 22.04, Java 17, extra system packages, cache)
- API key is saved locally in app private storage (not lost on restart)
- Calculator tool is integrated (simple math expressions are calculated locally)
- Better error messages for invalid key / quota / network / wrong model
- Cleaner dark UI with status bar
- Mic button present (shows clear message that speech recognition is future work)
- TTS “Speak Last” button using plyer
- Android back-button handling
- No API key is hardcoded or committed

## Features status

| Feature                        | Status                          |
|--------------------------------|---------------------------------|
| Dark futuristic UI             | Implemented                     |
| Hindi / English / Hinglish     | Via system prompt               |
| Gemini chat                    | Implemented                     |
| Text input + Send              | Implemented                     |
| Local SQLite history           | Implemented                     |
| Settings + API key save        | Implemented (local only)        |
| Calculator                     | Implemented (auto-detect math)  |
| Text-to-Speech                 | Implemented (plyer)             |
| Microphone / Speech-to-Text    | Stub (shows message)            |
| Loading / error status         | Implemented                     |
| Network error handling         | Implemented                     |
| Android back button            | Implemented                     |

## How to build APK (GitHub Actions)

1. Create a new GitHub repository (or use existing).
2. Upload **all files from this folder** to the **root** of the repository  
   (main.py and buildozer.spec must be at root, not inside another folder).
3. Go to **Actions** tab → select **Build Amie AI APK** → **Run workflow**.
4. Wait 15–40 minutes (first build is slower).
5. When green, download the artifact **amie-ai-debug-apk**.
6. Extract the `.apk` and install on your Android phone  
   (enable “Install from unknown sources” if asked).

## How to set Gemini API key

1. Open the installed Amie AI app.
2. Tap the ⚙ button.
3. Paste your Gemini API key (get it free from Google AI Studio).
4. Model default is `gemini-2.5-flash` (you can change it if needed).
5. Save. Key is stored only on your phone.

**Never** put your real API key inside any file that you push to GitHub.

## Important notes

- This is a **debug APK**. For Play Store you need a signed release build later.
- Speech recognition (mic) is intentionally not fully implemented yet — it needs extra native Android work.
- For public distribution of the app, a backend proxy is recommended so the API key is never inside the APK.

## Pydroid 3 testing

You can open the project folder in Pydroid 3 and run `main.py` for quick UI testing on the phone (Kivy plugin required). Full Android packaging still goes through GitHub Actions + Buildozer.

---

Made for beginners. Simple structure, clear errors, no magic.
