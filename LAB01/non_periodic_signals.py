# 2.4 Signals: Non-Periodic Signals
import numpy as np
import matplotlib.pyplot as plt

# Generate a random non-periodic signal
t = np.linspace(0, 1, 100)  # Time vector
signal = np.random.randn(100)  # Random signal

# Plot the signal
plt.plot(t, signal)
plt.title('Non-Periodic Random Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()
