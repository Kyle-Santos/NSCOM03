# 8.7 Coding Signals: PCM (Example 9)
import matplotlib.pyplot as plt
import numpy as np

# Parameters
max_frequency_hz = 4000  # Maximum frequency in Hz
bits_per_sample = 8  # Bits per sample

# Create the data for the plot
frequencies = np.linspace(0, max_frequency_hz, 400)
sampling_rates = 2 * frequencies
bit_rates = sampling_rates * bits_per_sample

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(frequencies, sampling_rates, label='Sampling Rate (samples/second)', color='blue')
plt.plot(frequencies, bit_rates, label='Bit Rate (bits/second)', color='red')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Rate')
plt.title('Relationship Between Frequency, Sampling Rate, and Bit Rate')
plt.ylim(0, max(bit_rates) * 1.2)  # Add some padding to the y-axis
plt.legend()
plt.margins(x=0)
plt.yticks(np.arange(0, 66000, 5000))
plt.grid(True)

plt.show()
