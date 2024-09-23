# 4.3 Distortion
import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequency = 4  # Frequency in Hz
sampling_rate = 100  # Sampling rate in Hz
duration = 1  # Duration of the signal in seconds
distortion_factor = 0.5  # Distortion factor

# Time vector
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Original sine wave
sine_wave = np.sin(2 * np.pi * frequency * t)

# Distorted sine wave (adding a harmonic)
distorted_sine_wave = sine_wave + distortion_factor * np.sin(2 * np.pi * 2 * frequency * t)

# Plotting
plt.figure(figsize=(10, 4))
plt.plot(t, sine_wave, label='Original Sine Wave')
plt.plot(t, distorted_sine_wave, label='Distorted Sine Wave')
plt.title('Distortion Example')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
