# 2.5 Signals: Sine Waves
import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0, 1, 0.0001)

# Sine wave with a frequency of 4 Hz (1 period every 0.25 seconds) with no shift
frequency = 4  # 4 Hz for 1/4 period per second
amplitude = np.sin(2 * np.pi * frequency * time)

# Plot the sine wave in its natural range of -1 to 1
plt.plot(time, amplitude, color='blue')
plt.title('Sine Wave (1/4 Period per Second)')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')

# Set y-axis from -1 to 1
plt.ylim(-1, 1)
plt.yticks([-1, -0.5, 0, 0.5, 1])

# Set x-axis ticks to 0, 0.25, 0.5, 0.75, 1
plt.xticks([0, 0.25, 0.5, 0.75, 1])

# Remove space between plot and the y-axis
plt.margins(x=0)

# Add grid
plt.grid(True)

# Show the plot
plt.show()
