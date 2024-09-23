# 2.3 Signals: Periodic Signals
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000, endpoint=False)
plt.plot(t, np.sin(2 * np.pi * 5 * t), label='Sine - 5 Hz')
plt.plot(t, np.cos(2 * np.pi * 10 * t), 'orange', label='Cosine - 10 Hz')
plt.legend()
plt.grid()
plt.show()
