import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import time

def plotsound(y, Fs):
    wait_time = 0.1  # Wait time between updates (in seconds)
    samples = int(np.ceil(Fs * wait_time))  # Number of samples per update

    plt.figure()
    plt.xlim([0, len(y)])
    plt.ylim([0.9 * np.min(y), 1.1 * np.max(y)])
    plt.title('Audio sample')
    plt.xlabel('Sample index')
    plt.ylabel('Amplitude')

    # Start audio playback
    sd.play(y, Fs)

    # Plot the audio signal in chunks
    for i in range(0, len(y) - samples, samples):
        plt.plot(np.arange(i, i + samples), y[i:i + samples], 'b')
        plt.pause(wait_time)

    # Wait for the audio to finish playing
    sd.wait()
    plt.show()

