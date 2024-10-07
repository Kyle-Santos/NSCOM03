# 8.3 Coding Signals: PCM (Example 6)
def calculate_sampling_rate(max_frequency_hz):
    # The Nyquist theorem states that the sampling rate should be at least twice the maximum frequency
    sampling_rate = 2 * max_frequency_hz
    return sampling_rate

# Parameter/s
max_frequency_hz = 200000  # Maximum frequency in Hz

# Calculate the sampling rate
sampling_rate = calculate_sampling_rate(max_frequency_hz)

# Print the result
print(f"The sampling rate is {sampling_rate} samples per second")