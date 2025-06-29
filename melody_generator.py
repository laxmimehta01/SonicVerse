from midiutil import MIDIFile

def generate_melody(output_file="melody.mid"):
    tempo = 75
    track = 0
    channel = 0
    volume = 110  # 🔊 Louder than before
    time = 0

    midi = MIDIFile(1)
    midi.addTempo(track, time, tempo)

    # Chords: Am – F – C – G
    chords = {
        'Am': [57, 60, 64],
        'F': [53, 57, 60],
        'C': [48, 52, 55],
        'G': [50, 55, 59]
    }

    # 🎵 Repeat chords multiple times
    progression = ['Am', 'F', 'C', 'G'] * 16  # n rounds = longer music

    for chord_name in progression:
        for note in chords[chord_name]:
            midi.addNote(track, channel, note, time, 2, volume)
        time += 2

    # Melody notes (loop over scale)
    melody = [69, 72, 74, 72, 71, 69, 67, 69] * 2

    melody_start = 4
    for i, note in enumerate(melody):
        midi.addNote(track, channel, note, melody_start + i * 0.5, 0.5, volume)

    with open(output_file, "wb") as f:
        midi.writeFile(f)

    print(f"\n✅ Melody generated and saved as: {output_file}")
