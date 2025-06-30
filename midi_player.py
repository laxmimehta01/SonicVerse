import pygame
import time

def play_midi(file_path):
    try:
        print(f"🎧 Playing {file_path}...")
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Wait for the music to finish
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        print("✅ Done playing.")
        pygame.quit()

    except Exception as e:
        print("❌ Error playing MIDI:", e)
