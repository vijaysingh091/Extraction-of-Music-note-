import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.fft import fft
from scipy.io.wavfile import write

# Function to convert frequency to note (define this based on your requirement)
def FreqToNote(freq):
    # Add logic to return the letter and frequency of the note
    # Example: (replace with correct mapping logic)
    notes = {440: 'A', 494: 'B'}
    closest_freq = min(notes.keys(), key=lambda x: abs(x - freq))
    return notes.get(closest_freq, 'Unknown'), closest_freq

# Set mute flag
mute = True  # Change to False if you want to play audio

# Load the audio file
song, Fs = sf.read('FurElise_Slow.mp3')
Fs = int(Fs * 4)  # Speed up song
plt.figure()
plt.plot(song[:, 0])
plt.title('Fur Elise, entire song')
plt.show()

# Set parameters
t1, t2 = int(2.9e6), int(4.9e6)
y = song[t1:t2]
n = y.shape[0]
t = np.linspace(t1, t2, n)

if not mute:
    sf.write('fur_elise_window.wav', y, Fs)

# Downsample by factor of m
m = 20
Fsm = int(Fs / m)
p = n // m
y_avg = np.array([np.mean(y[i*m:(i+1)*m]) for i in range(p)])

plt.figure()
plt.plot(np.linspace(0, 100, n), np.abs(y))
plt.plot(np.linspace(0, 100, p), np.abs(y_avg))
plt.title('Discrete notes of song')
plt.legend(['Original', '20-point averaged and down-sampled'])
plt.show()

if not mute:
    write('downsampled_audio.wav', Fsm, y_avg)

# Threshold to detect notes
y_thresh = np.zeros(p)
i = 0
while i < p:
    thresh = 5 * np.median(np.abs(y_avg[max(0, i-5000):i+1]))
    if np.abs(y_avg[i]) > thresh:
        y_thresh[i:i+500] = y_avg[i]
        i += 1400
    i += 1

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(np.abs(y_avg))
plt.title('Original song')
plt.ylim([0, 1.1 * max(y_avg)])

plt.subplot(2, 1, 2)
plt.plot(np.abs(y_thresh))
plt.title('Detected notes using moving threshold')
plt.show()

if not mute:
    write('threshold_notes.wav', Fsm, y_thresh)

# Find frequencies of each note
fundamentals = []
i = 0
while i < p:
    if y_thresh[i] != 0:
        note = []
        while i < p and (y_thresh[i] != 0 or len(note) > 0):
            note.append(y_thresh[i])
            if y_thresh[i] == 0:
                note = note[:-20]  # Trim end silence
            i += 1
        
        note_padded = np.pad(note, (0, len(note)), mode='constant')
        Note = fft(note_padded)
        f = np.linspace(0, Fs / 2, len(Note) // 2)
        peak_freq = f[np.argmax(np.abs(Note[:len(f)]))]

        if peak_freq > 20:
            fundamentals.append(peak_freq * 2)
            plt.figure()
            plt.plot(f, np.abs(Note[:len(f)]))
            plt.title(f'Fundamental frequency = {peak_freq * 2:.2f} Hz')
            plt.show()
    i += 1

# Recreate the song using detected notes
amp = 1
fs = 20500  # Sampling frequency for recreation
duration = 0.5  # Duration of each note
recreate_song = np.zeros(int(duration * fs * len(fundamentals)))

for i, freq in enumerate(fundamentals):
    letter, freq = FreqToNote(freq)
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    a = amp * np.sin(2 * np.pi * freq * t * 2)
    start_idx = int(i * fs * duration)
    recreate_song[start_idx:start_idx + len(a)] = a

    if not mute:
        write('recreated_note.wav', fs, a)
        sf.write('recreated_song.wav', recreate_song, fs)

print(f'Detected notes: {fundamentals}')
