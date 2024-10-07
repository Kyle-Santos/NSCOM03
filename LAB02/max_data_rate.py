# 3.2 Coding Signals: Data rate and Baude rate (Note on Bandwidth w Digital Signals, equation)
import math

def max_data_rate(bandwidth, modulation_levels):
  # Calculate the maximum data rate using the formula N_max = 2 * B * log2(L)
  max_data_rate = 2 * bandwidth * math.log2(modulation_levels)
  return max_data_rate

# Calculate the maximum data rate
max_data_r = max_data_rate(10000, 16)
print(f"The calculated maximum data rate is: {max_data_r} bits per second")