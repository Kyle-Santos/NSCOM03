# 8.7 Coding Signals: PCM (Example 9)
def calculate_sampling_rate(max_frequency_hz):
    # The Nyquist theorem states that the sampling rate should be at least twice the maximum frequency
    sampling_rate = 2 * max_frequency_hz
    return sampling_rate

def calculate_bit_rate(sampling_rate, bits_per_sample):
  return sampling_rate * bits_per_sample

# Parameter/s
max_frequency_hz = 4000  # Maximum frequency in Hz
bits_per_sample = 8  # Bits per sample

# Calculate the sampling rate
sampling_rate = calculate_sampling_rate(max_frequency_hz)
bit_rate = calculate_bit_rate(sampling_rate, bits_per_sample)

# Print the result
print(f"The sampling rate is {sampling_rate} samples per second")
print(f"The bit rate is {bit_rate} bits per second or {bit_rate / 1000} kbps")