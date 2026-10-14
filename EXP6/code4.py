
# FIR Band-Stop Filter Design using Hann Window
# Cutoff Frequencies = 3 kHz and 4 kHz

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Step 1: Define filter parameters
Fs = 10000          # Sampling frequency = 10 kHz
Fc1 = 3000          # Lower cutoff frequency = 3 kHz
Fc2 = 4000          # Upper cutoff frequency = 4 kHz
N = 31              # Number of filter taps

# Step 2: Design the FIR band-stop filter
b = firwin(
    numtaps=N,
    cutoff=[Fc1, Fc2],
    window='hann',
    pass_zero='bandstop',
    fs=Fs
)

# Step 3: Calculate frequency response
f, H = freqz(b, worN=2048, fs=Fs)

# Magnitude response
magnitude_db = 20 * np.log10(np.maximum(np.abs(H), 1e-10))

# Step 4: Plot Magnitude Response
plt.figure(figsize=(10, 5))
plt.plot(f, magnitude_db)
plt.title('FIR Band-Stop Filter - Magnitude Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 5: Plot Impulse Response
plt.figure(figsize=(9, 4))
plt.stem(np.arange(N), b)
plt.title('FIR Band-Stop Filter - Impulse Response')
plt.xlabel('Sample Number (n)')
plt.ylabel('Amplitude h[n]')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 6: Plot Phase Response
phase = np.unwrap(np.angle(H))

plt.figure(figsize=(9, 4))
plt.plot(f, phase)
plt.title('FIR Band-Stop Filter - Phase Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (radians)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 7: Print filter coefficients
print("FIR Band-Stop Filter Coefficients:")
for i, coeff in enumerate(b):
    print(f"h[{i}] = {coeff:.6f}")
