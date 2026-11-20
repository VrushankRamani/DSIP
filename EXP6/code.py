# FIR Low-Pass Filter Design using Hann Window
# Cutoff Frequency = 3 kHz
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz
# Step 1: Define filter parameters
Fs = 10000          # Sampling frequency = 10 kHz
Fc = 3000           # Cutoff frequency = 3 kHz
N = 31              # Number of filter taps
# Step 2: Design the FIR low-pass filter
b = firwin(
    numtaps=N,
    cutoff=Fc,
    window='hann',
    pass_zero='lowpass',
    fs=Fs
)
# Step 3: Calculate frequency response
f, H = freqz(b, worN=2048, fs=Fs)
# Magnitude response
magnitude_db = 20 * np.log10(np.maximum(np.abs(H), 1e-10))

# Impulse Response
plt.figure(figsize=(9, 4))
plt.stem(np.arange(N), b)
plt.title('Impulse Response')
plt.xlabel('Sample Number (n)')
plt.ylabel('Amplitude h[n]')
plt.grid(True)
plt.tight_layout()
plt.show()

# Magnitude Response
plt.figure(figsize=(9, 4))
plt.plot(f, magnitude_db)
plt.title('Magnitude Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.tight_layout()
plt.show()

