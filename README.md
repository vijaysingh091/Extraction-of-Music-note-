# Extraction-of-Music-note-
Audio Note Extraction and Analysis
This repository contains a set of Python scripts for extracting musical notes from audio files, analyzing the frequency components, and visualizing the waveform in real time. The code is a Python adaptation of MATLAB functions.
________________________________________
📁 Project Structure
bash
Copy code
├── main.py             # Main program for audio note extraction and frequency analysis
├── FreqToNote.py       # Function to map frequencies to musical notes
├── plotsound.py        # Function to play and plot the audio signal in real-time
├── FurElise_Slow.mp3   # Sample input audio file (optional)
├── requirements.txt    # Dependencies for the project
└── README.md           # Documentation of the project
________________________________________
🚀 How It Works
1.	main.py:
o	Reads an audio file and analyzes a specific window of the song.
o	Uses FFT to extract frequency components and down-sample the audio.
o	Applies a moving threshold to detect musical notes.
o	Recreates the song using detected fundamental frequencies.
2.	FreqToNote.py:
o	Converts a given frequency to its corresponding musical note using logarithmic mapping.
o	Returns both the note and the closest frequency.
3.	plotsound.py:
o	Plays the audio while plotting the waveform in real time.
o	Simulates real-time audio visualization with matplotlib and sounddevice.
________________________________________
📦 Dependencies
Install the required libraries using the following command:
bash
Copy code
pip install -r requirements.txt
requirements.txt:
Copy code
numpy
matplotlib
sounddevice
scipy
________________________________________
Usage
1.	Clone the Repository:
bash
Copy code
git clone https://github.com/your-username/audio-note-extraction.git
cd audio-note-extraction
2.	Run the Main Script:
bash
Copy code
python main.py
3.	Sample Usage of FreqToNote.py:
python
Copy code
from FreqToNote import FreqToNote

note, freq = FreqToNote(440)
print(f"Note: {note}, Frequency: {freq} Hz")  # Output: Note: A4, Frequency: 440 Hz
4.	Visualize and Play Audio:
python
Copy code
from plotsound import plotsound
import scipy.io.wavfile as wav

Fs, y = wav.read('FurElise_Slow.wav')
plotsound(y, Fs)
________________________________________
Features
•	Extract and recreate musical notes from any audio file.
•	Detect fundamental frequencies using FFT.
•	Visualize audio signals dynamically while playing them.
•	Identify musical notes based on frequency mappings.
________________________________________
Input Files
•	FurElise_Slow.mp3:
o	A sample audio file provided for testing.
o	You can replace it with your own .wav or .mp3 file.
________________________________________
Troubleshooting
•	If you encounter issues with audio playback, ensure the sounddevice library is properly installed and your audio device is configured.
•	If using a .wav file as input, ensure it is in the correct format (int16 or float32).
________________________________________
License
This project is licensed under the MIT License - see the LICENSE file for details.
________________________________________
Contributing
Feel free to submit issues or pull requests if you encounter any bugs or have feature requests.
________________________________________
Author
•	Vijay Bhushan Singh
________________________________________
