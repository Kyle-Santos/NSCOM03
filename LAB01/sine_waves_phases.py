# 2.6 Signals: Sine Waves – Phase (Cosine Waves: Sine Waves but Degrees different)
import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequency = 4  # Frequency in Hz
sampling_rate = 100  # Sampling rate in Hz
duration = 1  # Duration of the signal in seconds

# Time vector
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Degrees to radians conversion
degrees = [0, 90, 180, 270]
radians = [np.deg2rad(deg) for deg in degrees]

# Create a figure with 4 subplots
fig, axs = plt.subplots(4, 1, figsize=(8, 12))

# Plot each sine wave starting at the specified angle
for i, rad in enumerate(radians):
    # Shift the sine wave by the corresponding angle
    sine_wave = np.sin(2 * np.pi * frequency * t + rad)

    # Plot the sine wave in the corresponding subplot
    axs[i].plot(t, sine_wave)
    axs[i].set_title(f'Sine Wave (Starting at {degrees[i]}°)')
    axs[i].set_xlabel('Time [s]')
    axs[i].set_ylabel('Amplitude')
    axs[i].grid(True)

# Adjust layout for better visualization
plt.tight_layout()
plt.show()
