# 5.3 Shannon Capacity
import numpy as np
import matplotlib.pyplot as plt

# Define bandwidths for which we'll calculate capacity
bandwidths = [1000, 2000, 3000, 4000]  # in Hz
snr_dB = np.arange(0, 30, 1)  # SNR values in dB (0 to 30 dB)

# Convert SNR from dB to linear scale
snr_linear = 10 ** (snr_dB / 10)

# Shannon Capacity formula to calculate channel capacity
def shannon_capacity(bandwidth, snr):
    return bandwidth * np.log2(1 + snr)

# Plot
plt.figure(figsize=(10, 6))

for bandwidth in bandwidths:
    capacities = shannon_capacity(bandwidth, snr_linear)
    plt.plot(snr_dB, capacities, label=f'Bandwidth = {bandwidth} Hz')

plt.title('Shannon Channel Capacity vs SNR')
plt.xlabel('SNR (dB)')
plt.ylabel('Channel Capacity (bps)')
plt.legend()
plt.grid(True)
plt.show()
