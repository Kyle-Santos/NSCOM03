# 4.4 Noise
import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequency = 4  # Frequency in Hz
sampling_rate = 100  # Sampling rate in Hz
duration = 1  # Duration of the signal in seconds
noise_amplitude = 0.5  # Amplitude of the noise

# Time vector
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Original sine wave
sine_wave = np.sin(2 * np.pi * frequency * t)

# Noisy sine wave
noise = noise_amplitude * np.random.randn(len(t))
noisy_sine_wave = sine_wave + noise

# Plotting
plt.figure(figsize=(10, 4))
plt.plot(t, sine_wave, label='Original Sine Wave')
plt.plot(t, noisy_sine_wave, label='Noisy Sine Wave')
plt.title('Noise Example')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
