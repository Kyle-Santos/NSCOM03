# 2.8 Composite Signals
import numpy as np
import matplotlib.pyplot as plt

# Time from 0 to 1 second, with a step of 0.001 seconds for smooth plotting
time = np.arange(0, 1, 0.001)

# Define the fundamental frequency
f = 4  # 4 Hz

# Create three sine waves with frequencies f, 3f, and 9f, each with different amplitudes
sine_wave_f = 1 * np.sin(2 * np.pi * f * time)      # Fundamental frequency
sine_wave_3f = 0.5 * np.sin(2 * np.pi * 3 * f * time)  # 3 times the fundamental frequency
sine_wave_9f = 0.2 * np.sin(2 * np.pi * 9 * f * time)  # 9 times the fundamental frequency

# Composite signal: sum of all three sine waves
composite_signal = sine_wave_f + sine_wave_3f + sine_wave_9f

# Plot the composite signal
plt.figure(figsize=(10, 6))
plt.plot(time, composite_signal, label='Composite Signal', color='purple')

# Plot the individual sine waves for reference
plt.plot(time, sine_wave_f, '--', label='Fundamental Frequency (f)', color='blue')
plt.plot(time, sine_wave_3f, '--', label='3rd Harmonic (3f)', color='green')
plt.plot(time, sine_wave_9f, '--', label='9th Harmonic (9f)', color='red')

# Add title and labels
plt.title('Composite Signal (Combination of f, 3f, and 9f)')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')

# Add legend
plt.legend()

# Remove space between plot and the y-axis
plt.margins(x=0)
plt.xticks([0, 0.25, 0.5, 0.75, 1])

# Add grid
plt.grid(True)

# Show the plot
plt.show()
