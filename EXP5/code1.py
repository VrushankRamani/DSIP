import numpy as np 
import matplotlib.pyplot as plt 
 
signal = np.array([1, 2, 3, 4, 5, 6, 7, 8]) 
 
# Compute the FFT of the signal fft_result = np.fft.fft(signal) 
 
# Compute the magnitude and Phase spectrum of the FFT result 
magnitude_spectrum = np.abs(fft_result) 
Phase_spectrum = np.angle(fft_result) 
 
# Compute the IFFT of the FFT result reconstructed_signal = np.fft.ifft(fft_result) 
 
plt.figure(figsize=(12, 22)) 
 
# 1. Original Discrete Time Signal plt.subplot(5, 1, 1) plt.stem(signal) plt.title('Original Discrete Time Signal') plt.xlabel('Sample') plt.ylabel('Amplitude') plt.grid(True) 
 
for i, val in enumerate(signal): 
    plt.text(i, val + 0.2, f'{val}', ha='center', va='bottom', fontsize=9) 
 
 
# 2. FFT Real and Imaginary Components plt.subplot(5, 1, 2) plt.stem(fft_result.real, linefmt='b-', markerfmt='bo', basefmt=' ') plt.stem(fft_result.imag, linefmt='r-', markerfmt='rx', basefmt=' ') 
 
plt.title('FFT Real (Blue) and Imaginary (Red) Components') 
plt.xlabel('Frequency Bin') 
plt.ylabel('Component Value') 
plt.grid(True) 
 
for i, val in enumerate(fft_result.real):  
    plt.text(i, val + 0.2, f'R:{val:.2f}',          
             ha='center', va='bottom', fontsize=9, color='blue') 
 
for i, val in enumerate(fft_result.imag):    
    plt.text(i, val - 0.5, f'I:{val:.2f}',        
             ha='center', va='top', fontsize=9, color='red') 
 
 
# 3. FFT Magnitude plt.subplot(5, 1, 3) plt.stem(magnitude_spectrum) plt.title('FFT Magnitude') plt.xlabel('Frequency Bin') plt.ylabel('Magnitude') plt.grid(True) 
 
for i, val in enumerate(magnitude_spectrum):  
    plt.text(i, val + 0.2, f'{val:.2f}',        
             ha='center', va='bottom', fontsize=9) 
 
 
# 4. FFT Phase Spectrum plt.subplot(5, 1, 4) plt.stem(Phase_spectrum) plt.title('FFT Phase Spectrum') plt.xlabel('Frequency Bin') plt.ylabel('Phase (radians)') plt.grid(True) 
 
for i, val in enumerate(Phase_spectrum):  
    plt.text(i, val + 0.1, f'{val:.2f}',       
             ha='center', va='bottom', fontsize=9) 
 

 
# 5. Reconstructed Signal plt.subplot(5, 1, 5) plt.stem(reconstructed_signal.real) plt.title('Reconstructed Signal') plt.xlabel('Sample') plt.ylabel('Amplitude') plt.grid(True) 
 
for i, val in enumerate(reconstructed_signal.real):    
    plt.text(i, val + 0.2, f'{val:.2f}',            
             ha='center', va='bottom', fontsize=9) 
 
plt.tight_layout() 
plt.show() 
