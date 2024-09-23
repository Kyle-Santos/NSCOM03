# 2.9 Bandwidth
import numpy as np
import matplotlib.pyplot as plt

# Define a denser frequency range
frequencies = np.arange(1000, 5001, 100)  # More frequent points between 1000 and 5000 Hz
amplitudes = np.abs(np.sin(frequencies * np.pi / 5000)) * 10  # Keeping the same amplitude modulation

# Create the plot
plt.figure(figsize=(8, 4))
plt.stem(frequencies, amplitudes, linefmt='b-', markerfmt='bo', basefmt='k')
plt.xlim(800, 5200)
plt.ylim(0, 11)

# Adding labels and title
plt.title('Bandwidth of a Periodic Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.grid(True)
plt.show()
