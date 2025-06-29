print("🎤 Welcome to SonicVerse – Turn your words into music!")
choice = input("Do you want to (1) type your lyrics or (2) upload from file? Enter 1 or 2: ")

lyrics = ""

if choice == '1':
    lines = []
    print("\n✍️ Type your lyrics below (type 'END' to finish):")
    while True:
        text = input()
        if text.strip() == 'END':
            break
        lines.append(text)
    lyrics = "\n".join(lines)
    print("\n🎶 Your Lyrics:\n" + lyrics)

elif choice == '2':
    file_path = input("Enter your lyrics file path : ")
    try:
        with open(file_path , 'r') as f:
            lyrics = f.read()
        print("\n🎶 Your Lyrics:\n" + lyrics)
    except FileNotFoundError:
        print("❌ File not found. Exiting.")
        lyrics = None

else:
    print("Invalid Choice")
    lyrics = None

if __name__ == "__main__" and lyrics:
    with open("lyrics.txt", "w") as f:
        f.write(lyrics)
        print("\n✅ Lyrics saved. Ready to turn this into a melody in the next step!")
