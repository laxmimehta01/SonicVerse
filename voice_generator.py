import pyttsx3

def speak_lyrics(lyrics):
    try:
        print("🗣️ Speaking lyrics...\n")
        engine = pyttsx3.init()
        rate = 130  # words per minute
        engine.setProperty('rate', rate)
        engine.setProperty('volume', 0.9)

        # Estimate duration (in seconds)
        words = len(lyrics.split())
        estimated_duration = words / (rate / 60)

        engine.say(lyrics)
        engine.runAndWait()
        print("✅ Done speaking.")

        return estimated_duration

    except Exception as e:
        print("❌ Error with text-to-speech:", e)
        return 5  # fallback
