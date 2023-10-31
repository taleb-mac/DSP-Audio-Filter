from scipy.signal import butter, lfilter
from scipy.io import wavfile

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def create_filtered_wav(input_wav_path, output_wav_path, cutoff, order=5):
    sample_rate, data = wavfile.read(input_wav_path)
    filtered_data = lowpass_filter(data, cutoff, sample_rate, order)
    wavfile.write(output_wav_path, sample_rate, filtered_data.astype(data.dtype))

def main():
    input_wav_path = r'C:\Users\alref\OneDrive\Desktop\DSP\audio_clips\hornet_gitgud.wav'
    output_wav_path = r'C:\Users\alref\OneDrive\Desktop\DSP\audio_clips\hornet_gitgud_filtered.wav'
    cutoff = 10000
    create_filtered_wav(input_wav_path, output_wav_path, cutoff)

if __name__ == "__main__":
    main()




