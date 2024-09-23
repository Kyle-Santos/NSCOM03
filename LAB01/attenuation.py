# 4.1 Attenuation
import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequency = 4  # Frequency in Hz
sampling_rate = 100  # Sampling rate in Hz
duration = 1  # Duration of the signal in seconds
attenuation_factor = 0.5  # Attenuation factor

# Time vector
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Original sine wave
sine_wave = np.sin(2 * np.pi * frequency * t)

# Attenuated sine wave
attenuated_sine_wave = sine_wave * attenuation_factor

# Plotting
plt.figure(figsize=(10, 4))
plt.plot(t, sine_wave, label='Original Sine Wave')
plt.plot(t, attenuated_sine_wave, label='Attenuated Sine Wave')
plt.title('Attenuation Example')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()