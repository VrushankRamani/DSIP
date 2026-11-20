import os 
import subprocess
import numpy as np 
import librosa 
import librosa.display
import matplotlib.pyplot as plt
import soundfile as sf 
from scipy.signal import butter, sosfiltfilt 
 
# 1. Load the same MP3 song 
filename = "/content/iphone-remix-68028.mp3" 
 
y, sr = librosa.load(filename, sr=None, mono=True) 
 
print("Sample rate:", sr, "Hz") 
print("Duration:", round(len(y) / sr, 2), "seconds") 
 
# 2. Band-pass filter function
def bandpass_filter(data, lowcut, highcut, fs, order=6): 
    sos = butter(         order, [lowcut, highcut],         btype="bandpass", fs=fs, output="sos" 
    ) 
    return sosfiltfilt(sos, data) 
 
# 3. Band-stop filter function
def bandstop_filter(data, lowcut, highcut, fs, order=6): 
    sos = butter(         order, [lowcut, highcut],         btype="bandstop", fs=fs, output="sos" 
    ) 
    return sosfiltfilt(sos, data) 
 
# Check valid frequency range if sr / 2 <= 3400: 
    raise ValueError("Sample rate is too low for a 3400 Hz cutoff.") 
 
# 4. Estimate vocal frequency band  vocal_audio = bandpass_filter(y, 300, 3400, sr) 
 
# 5. Suppress the same frequency band 
# This retains frequencies below 300 Hz and above 3400 Hz background_audio = bandstop_filter(y, 300, 3400, sr) 
 
# 6. Save audio as WAV first sf.write("/content/filtered_vocals.wav", vocal_audio, sr) sf.write("/content/background_music.wav", background_audio, sr) 
 
# 7. Convert WAV files to MP3 using FFmpeg
subprocess.run([ 
    "ffmpeg", "-y", "-i", "/content/filtered_vocals.wav", 
    "-codec:a", "libmp3lame", "-b:a", "192k", 
    "/content/filtered_vocals.mp3" 
], check=True) 
 
subprocess.run([ 
    "ffmpeg", "-y", "-i", "/content/background_music.wav", 
    "-codec:a", "libmp3lame", "-b:a", "192k", 
    "/content/background_music.mp3" 
], check=True) 
 
print("Both MP3 files saved successfully!") 
 
# 8. Plot spectrograms 
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
plt.title(plt.title(title))     
plt.tight_layout() 
plt.show() 
 
plot_spectrogram(y, sr, "Original Song") 
plot_spectrogram(vocal_audio, sr, "Estimated Vocals (300-3400 Hz)") 
plot_spectrogram(background_audio, sr, "Background-Focused Audio") 
 
