# 2.2 Signals: Digital Signals
import numpy as np
import matplotlib.pyplot as plt

values = [1, 0, 1, 2, 0, -1, 0, 2] # Digital signal values

# Create time points for each value
time = np.arange(len(values))

# Plot the digital signal
plt.step(time, values, where='mid', label='Digital Signal', linewidth=2)

# Adding labels and title
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Digital Signal')

plt.legend()
plt.show()
