import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from audio_filter import lowpass_filter

def read_audio_file(file_path):
    sample_rate, data = wavfile.read(file_path)
    return sample_rate, data

def to_mono(audio_data):
    if len(audio_data.shape) > 1:
        return np.mean(audio_data, axis=1)
    return audio_data

def calculate_fft(audio_data, sample_rate):
    n = len(audio_data)
    freq = np.fft.fftfreq(n, d=1/sample_rate)
    magnitude = np.abs(np.fft.fft(audio_data)) / n
    return freq[:n // 2], magnitude[:n // 2]  

def plot_frequency_response(original_data, filtered_data, fs, title1='Original Audio Spectrum', title2='Filtered Audio Spectrum'):
    def plot_spectrum(data, fs, title, subplot_position):
        freq, magnitude = calculate_fft(data, fs)
        plt.subplot(1, 2, subplot_position)
        plt.plot(freq, magnitude, color='blue')
        plt.title(title)
        plt.xlabel('Freq (Hz)')
        plt.ylabel('Magnitude')

    plt.figure(figsize=(12, 6))
    plot_spectrum(original_data, fs, title1, 1)
    plot_spectrum(filtered_data, fs, title2, 2)

    plt.tight_layout()
    plt.show()

def main():
    file_path = r'C:\Users\alref\OneDrive\Desktop\DSP\audio_clips\hornet_gitgud.wav'
    sample_rate, data = read_audio_file(file_path)
    mono_data = to_mono(data)
    filtered_data = lowpass_filter(mono_data, 1000, sample_rate)
    plot_frequency_response(mono_data, filtered_data, sample_rate)

if __name__ == "__main__":
    main()

    

