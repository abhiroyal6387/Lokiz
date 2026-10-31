import json
import urllib.request
import urllib.error


class Gemini:
    """Simple Gemini REST client using generateContent endpoint."""

    def __init__(self, cfg):
        self.key = (cfg.get("api_key") or "").strip()
        # Safe default that is currently available (Oct 2026)
        self.model = (cfg.get("model") or "gemini-2.5-flash").strip()

    def ask(self, history, prompt):
        if not self.key:
            raise RuntimeError("API key not configured. Open Settings and paste your Gemini API key.")

        contents = []
        for role, text in history:
            contents.append({
                "role": "user" if role == "user" else "model",
                "parts": [{"text": str(text)[:5000]}]
            })
        contents.append({
            "role": "user",
            "parts": [{"text": str(prompt)[:5000]}]
        })

        body = {
            "systemInstruction": {
                "parts": [{
                    "text": (
                        "You are Amie, a helpful personal AI assistant. "
                        "You understand and reply in Hindi, English and Hinglish naturally. "
                        "Be honest about your limitations. Keep answers clear and useful. "
                        "If the user asks a simple calculation you may still answer it."
                    )
                }]
            },
            "contents": contents,
            "generationConfig": {
                "maxOutputTokens": 800,
                "temperature": 0.7
            }
        }

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent"
        data = json.dumps(body).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "x-goog-api-key": self.key
            },
            method="POST"
        )

        try:
            with urllib.request.urlopen(req, timeout=40) as resp:
                result = json.loads(resp.read().decode("utf-8"))
            candidates = result.get("candidates") or []
            if not candidates:
                raise RuntimeError("Empty response from Gemini")
            parts = candidates[0].get("content", {}).get("parts") or []
            if not parts:
                raise RuntimeError("No text in Gemini response")
            return parts[0].get("text", "").strip() or "(empty reply)"

        except urllib.error.HTTPError as e:
            if e.code == 429:
                raise RuntimeError("Gemini quota / rate limit reached. Try again later.")
            if e.code == 404:
                raise RuntimeError(f"Model '{self.model}' not found. Check model name in Settings.")
            if e.code in (401, 403):
                raise RuntimeError("API key invalid or access denied. Check your key.")
            try:
                err_body = e.read().decode("utf-8", errors="ignore")[:300]
            except Exception:
                err_body = ""
            raise RuntimeError(f"Gemini HTTP {e.code}: {err_body}")

        except (urllib.error.URLError, TimeoutError, OSError):
            raise RuntimeError("Network error or timeout. Check internet connection.")
