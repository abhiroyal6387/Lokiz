def speak(text):
    """Speak text using platform TTS if available (plyer)."""
    if not text:
        return
    try:
        from plyer import tts
        tts.speak(str(text)[:500])
    except Exception:
        # Silently ignore if TTS is unavailable on this device
        pass
