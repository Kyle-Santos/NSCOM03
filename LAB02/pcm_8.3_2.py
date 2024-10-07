# 8.3 Coding Signals: PCM (Example 6)
import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 8000  # Sampling rate in Hz
t_max = 0.01  # Maximum time in seconds
t = np.linspace(0, t_max, int(fs * t_max), endpoint=False)  # Time vector

# Generate an analog signal (e.g., a sine wave)
frequency = 4000  # Frequency of the analog signal in Hz
analog_signal = np.sin(2 * np.pi * frequency * t)

# Sample the analog signal
sampled_signal = analog_signal[::int(fs/fs)]  # Downsample the signal

# Time vector for the sampled signal
t_sampled = np.linspace(0, t_max, len(sampled_signal), endpoint=False)

# Plot the signals
plt.figure(figsize=(12, 6))

# Plot both signals
plt.plot(t, analog_signal, 'k', label='Analog Signal')
# plt.plot(t_sampled, sampled_signal, 'ro--', label='Sampled Signal')
plt.stem(t_sampled, sampled_signal, label='Sampled Signal', linefmt='o--', basefmt=" ", markerfmt="ro")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Analog Signal and Sampled Signal')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
