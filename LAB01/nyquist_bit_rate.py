# 5.2 Nyquist Bit Rate
import numpy as np
import matplotlib.pyplot as plt

# Define bandwidths for which we'll calculate bit rate
bandwidths = [1000, 2000, 3000, 4000]  # in Hz
levels = np.arange(2, 33, 2)  # Signal levels from 2 to 32 (even numbers)

# Nyquist formula to calculate bit rate
def nyquist_bit_rate(bandwidth, levels):
    return 2 * bandwidth * np.log2(levels)

# Plot
plt.figure(figsize=(10, 6))

for bandwidth in bandwidths:
    bit_rates = nyquist_bit_rate(bandwidth, levels)
    plt.plot(levels, bit_rates, label=f'Bandwidth = {bandwidth} Hz')

plt.title('Nyquist Bit Rate vs Signal Levels')
plt.xlabel('Number of Signal Levels (M)')
plt.ylabel('Bit Rate (bps)')
plt.legend()
plt.grid(True)
plt.show()
