import pygame
import time
import threading
from melody_generator import generate_melody
from voice_generator import speak_lyrics

def play_music_with_fade(filepath, fade_after):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()
    print("🎶 Music started...\n")
    time.sleep(fade_after)
    pygame.mixer.music.fadeout(3000)
    time.sleep(3)
    pygame.mixer.quit()

# --- Main Flow ---

print("🎤 Welcome to SonicVerse – Turn your words into music!")
choice = input("Do you want to (1) type your lyrics or (2) upload from file? Enter 1 or 2: ")

lyrics = ""

if choice == '1':
    lines = []
    print("\n✍️ Type your lyrics below (type 'END' to finish):")
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)
    lyrics = "\n".join(lines)

elif choice == '2':
    file_path = input("Enter your lyrics file path : ")
    try:
        with open(file_path, 'r') as f:
            lyrics = f.read()
    except FileNotFoundError:
        print("❌ File not found. Exiting.")
        lyrics = ""

else:
    print("❌ Invalid Choice")
    lyrics = ""

# MAIN EXECUTION
if __name__ == "__main__" and lyrics.strip():
    with open("lyrics.txt", "w") as f:
        f.write(lyrics)

    print("\n📝 Your Lyrics:\n")
    print(lyrics)

    output_file = "eyeliner_theme.mid"
    generate_melody(output_file)

    # --- START TTS THREAD ---
    voice_thread = threading.Thread(target=speak_lyrics, args=(lyrics,))
    voice_thread.start()

    # --- Delay music slightly so voice starts first ---
    time.sleep(0.5)

    # --- Start music in main thread ---
    voice_duration = len(lyrics.split()) / (130 / 60)  # ~TTS timing
    play_music_with_fade(output_file, voice_duration)

    voice_thread.join()
    print("\n✅ Done – Lyrics and music played in sync with fade-out.")
