import tkinter as tk
from tkinter import filedialog, messagebox
import os
from audio_compare import read_audio_file, to_mono, plot_frequency_response
from audio_filter import lowpass_filter, create_filtered_wav

class AudioFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Filter App")
        self.root.geometry("500x250")  # Set the window size
        self.root.resizable(False, False)  # Disable resizing

        self.file_path = tk.StringVar()
        self.cutoff_freq = tk.DoubleVar(value=1000)

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True, fill=tk.BOTH)

        tk.Label(frame, text="Select Audio File:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w")
        entry_file_path = tk.Entry(frame, textvariable=self.file_path, width=40, font=("Helvetica", 10))
        entry_file_path.grid(row=1, column=0, pady=(0, 10))
        tk.Button(frame, text="Browse", command=self.browse_file).grid(row=1, column=1, padx=10, pady=(0, 10))
        
        tk.Label(frame, text="Cutoff Frequency (Hz):", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w")
        entry_cutoff = tk.Entry(frame, textvariable=self.cutoff_freq, width=15, font=("Helvetica", 10))
        entry_cutoff.grid(row=3, column=0, pady=(0, 20), sticky="w")

        tk.Button(frame, text="Apply Filter and Plot", command=self.plot_filter, bg="#4CAF50", fg="white", width=20, height=2).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        tk.Button(frame, text="Apply Filter and Save", command=self.save_filter, bg="#2196F3", fg="white", width=20, height=2).grid(row=4, column=0, padx=10, pady=10, sticky="e")

    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=(("WAV files", "*.wav"), ("All files", "*.*")))
        if filename:
            self.file_path.set(filename)

    def plot_filter(self):
        if os.path.exists(self.file_path.get()):
            sample_rate, data = read_audio_file(self.file_path.get())
            data = to_mono(data)
            filtered_data = lowpass_filter(data, self.cutoff_freq.get(), sample_rate)
            plot_frequency_response(data, filtered_data, sample_rate)
        else:
            messagebox.showerror("Error", "File not found!")

    def save_filter(self):
        if os.path.exists(self.file_path.get()):
            sample_rate, data = read_audio_file(self.file_path.get())
            data = to_mono(data)

            output_file_path = self.file_path.get().replace(".wav", "_filtered.wav")
            create_filtered_wav(self.file_path.get(), output_file_path, self.cutoff_freq.get())
            messagebox.showinfo("Success", f"Filtered audio saved as: {output_file_path}")
        else:
            messagebox.showerror("Error", "File not found!")

def main():
    app = AudioFilterApp(tk.Tk())
    tk.mainloop()

if __name__ == "__main__":
    main()
