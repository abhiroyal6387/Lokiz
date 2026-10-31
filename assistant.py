from ai.gemini_provider import Gemini
from tools.calculator import calculate


class Assistant:
    def __init__(self, cfg, db):
        self.cfg = cfg
        self.db = db
        self.ai = Gemini(cfg)

    def ask(self, prompt):
        # Simple local calculator shortcut for pure math expressions
        text = prompt.strip()
        if self._looks_like_math(text):
            try:
                result = calculate(text)
                return f"Calculation result: {result}"
            except Exception:
                pass  # fall through to Gemini

        history = self.db.latest(8)
        # Remove the last user message if it was just added (avoid duplicate)
        if history and history[-1][0] == "user" and history[-1][1] == prompt:
            history = history[:-1]
        return self.ai.ask(history, prompt)

    def _looks_like_math(self, text):
        if not text or len(text) > 60:
            return False
        allowed = set("0123456789+-*/(). %")
        return all(c in allowed or c.isspace() for c in text) and any(c.isdigit() for c in text)
