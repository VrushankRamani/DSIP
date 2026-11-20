
import os 
import numpy as np 
import librosa 
import librosa.display 
import matplotlib.pyplot as plt
import soundfile as sf 
from scipy.signal import butter, sosfiltfilt 
 
# Load MP3 song filename = "/content/iphone-remix-68028.mp3" 
 
y, sr = librosa.load(filename, sr=None, mono=True) 
 
print("Sample rate:", sr, "Hz") 
print("Duration:", round(len(y) / sr, 2), "seconds") 
 
# Low-pass filter function def lowpass_filter(data, cutoff, fs, order=6):     sos = butter(order, cutoff, btype="lowpass",                  fs=fs, output="sos")     return sosfiltfilt(sos, data) 
 
# Apply three cutoff frequencies cutoffs = [500, 1500, 3000] 
 
for cutoff in cutoffs: 
    filtered = lowpass_filter(y, cutoff, sr) 
 
    # Save filtered audio     output_file = f"/content/lowpass_{cutoff}Hz.wav"     sf.write(output_file, filtered, sr) 
 
    print("Saved:", output_file) 
 
    # Plot waveform 
    time = np.arange(len(filtered)) / sr 
 
    plt.figure(figsize=(10, 3))    
    plt.plot(time, filtered)    
    plt.title(f"Low-Pass Filter - {cutoff} Hz")   
    plt.xlabel("Time (seconds)")   
    plt.ylabel("Amplitude")   
    plt.tight_layout()   
    plt.show() 
 
# Display spectrograms 
def plot_spectrogram(signal, sr, title): 
    D = librosa.amplitude_to_db(        
                                np.abs(librosa.stft(signal)), ref=np.max 
    ) 
 
    plt.figure(figsize=(10, 4))   
    librosa.display.specshow( 
        D, sr=sr, x_axis="time", y_axis="hz" 
    ) 
    plt.ylim(0, min(8000, sr / 2))   
    plt.colorbar(format="%+2.0f dB") 
    plt.title(title)   
    plt.tight_layout()    
    plt.show() 
 
plot_spectrogram(y, sr, "Original Song") 
 
for cutoff in cutoffs:
    filtered = lowpass_filter(y, cutoff, sr)     
    plot_spectrogram(         filtered, sr, f"Low-Pass Filter - {cutoff} Hz" 
    ) 
 
print("Part (a) completed successfully!") 
