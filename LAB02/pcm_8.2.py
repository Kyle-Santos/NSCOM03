# 8.2 Coding Signals: PCM (Example 5)
import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Standard sampling rate
f = 1  # Frequency of the sine wave

# Time vector
T = 1 / f * 3 # Second
t = np.linspace(0, T, fs, endpoint=False)  # Time vector at standard sampling rate

# Sine wave
y = np.sin(2 * np.pi * f * t)

# Sampling at different rates
fs_nyquist = 2 * f  # Nyquist rate
fs_oversampling = 4 * f  # oversampling
fs_undersampling = f # undersampling

# Time vectors for different sampling rates
t_nyquist = np.arange(0.25, T, 1 / int(fs_nyquist))
t_oversampling = np.arange(0, T, 1 / int(fs_oversampling))
t_undersampling = np.arange(0.25, T, 0.75 / int(fs_undersampling))

# Sampled sine waves
y_nyquist = np.sin(2 * np.pi * f * t_nyquist)
y_oversampling = np.sin(2 * np.pi * f * t_oversampling)
y_undersampling = np.sin(2 * np.pi * f * t_undersampling)

# Plotting
plt.figure(figsize=(12, 8))

# Original sine wave
plt.subplot(3, 1, 1)
plt.plot(t, y, 'k', label='Original Sine Wave')
plt.plot(t_nyquist, y_nyquist, 'ro--', label='Sampled at Nyquist Rate')
plt.title('Nyquist Rate Sampling (fs = 2f)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend(loc='upper right')
plt.margins(x=0)
plt.xticks(np.arange(0, 3.1, 0.25))

# Oversampling
plt.subplot(3, 1, 2)
plt.plot(t, y, 'k', label='Original Sine Wave')
plt.plot(t_oversampling, y_oversampling, 'ro--', label='Sampled at 2x Nyquist Rate')
plt.title('Oversampling (fs = 4f)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend(loc='upper right')
plt.margins(x=0)
plt.xticks(np.arange(0, 3.1, 0.25))

# Undersampling
plt.subplot(3, 1, 3)
plt.plot(t, y, 'k', label='Original Sine Wave')
plt.plot(t_undersampling, y_undersampling, 'ro--', label='Sampled at Half Nyquist Rate')
plt.title('Undersampling (fs = f)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend(loc='upper right')
plt.margins(x=0)
plt.xticks(np.arange(0, 3.1, 0.25))

plt.tight_layout()
plt.show()
