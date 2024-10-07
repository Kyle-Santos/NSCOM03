# 6.3 Coding Signals: Polar (Example 3)
import baud_rate

# Parameters
data_rate_bps = 1 * 1000000  # Data rate in bps
C = 1/2  # case factor
R = 1  # Code rate (assuming no coding, so R = 1)

# Calculate the average signal rate and minimum bandwidth
avg_signal_rate = baud_rate(data_rate_bps, C, R)
min_bandwidth = avg_signal_rate

# Print the results
print(f"Average signal rate: {avg_signal_rate} kbaud")
print(f"Minimum bandwidth: {min_bandwidth} kHz")