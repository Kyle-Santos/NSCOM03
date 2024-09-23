# 3.1 Baseband Transmission
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

# Changed input signal values
input_signal = np.array([0, 0.5, -0.5, 0.5, -0.5, 0.5, 0, -0.5, 0.5, 0])

# Plot the hardcoded input signal
plt.figure(figsize=(10, 6))

# Input signal plot
plt.subplot(2, 1, 1)
plt.step(t, input_signal, where='post', label='Baseband Transmission Input Signal', color='b')
plt.title('Baseband Transmission')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.xlim(0.0, 1.0)  # Set x-axis limits
plt.legend()

fs = 1000
f2 = 10
nyq = 0.5 * fs
low = f2 / nyq
b, a = signal.butter(4, low, btype='low')

t_interpolated = np.linspace(0, 1, fs, endpoint=False)
input_signal_interpolated = np.interp(t_interpolated, t, input_signal)

output_signal = signal.filtfilt(b, a, input_signal_interpolated)

plt.subplot(2, 1, 2)
plt.plot(t_interpolated, output_signal, label='Output Signal', color='r')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.xlim(0.0, 1.0)  # Set x-axis limits
plt.legend()

plt.tight_layout()
plt.show()