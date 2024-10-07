# 3.1 Coding Signals: Data rate and Baude rate (Example 1)
def baud_rate(data_rate, case_factor, data_signal_ratio):
  # Calculate the baud rate using the formula S = c * N * 1/r bauds
  baud_rate = case_factor * data_rate * (1 / data_signal_ratio)
  return baud_rate / 1000 # kbaud rate result

# Calculate the baud rate
baudrate = baud_rate(100000, 0.5, 1.0)
print(f"The calculated baud rate is: {baudrate} bauds")
print(f"The calculated baud rate is: {baudrate/1000} kbauds")