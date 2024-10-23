def ones_complement(n, bits=4):
    """Calculate the one's complement of a number."""
    return n ^ ((1 << bits) - 1)

def wrap_sum(sum_value, bits=4):
    """Wrap the sum to fit within the specified number of bits."""
    bin_sum = bin(sum_value)[2:]

    if len(bin_sum) > 4:
      first_2_bits = int(bin_sum[:2], 2)
      last_bits = int(bin_sum[2:], 2)
      wrapped_sum = first_2_bits + last_bits
    else:
      wrapped_sum = int(bin_sum)

    return wrapped_sum

def calculate_checksum(data):
    """Calculate the checksum for the given data."""
    checksum = 0
    for num in data:
        checksum += num
    wrapped_sum = wrap_sum(checksum)
    checksum = ones_complement(wrapped_sum)
    return checksum

def verify_checksum(data_with_checksum):
    """Verify the checksum for the given data."""
    checksum = data_with_checksum[-1]
    data = data_with_checksum[:-1]
    total = sum(data) + checksum
    wrapped_total = wrap_sum(total)
    calculated_checksum = ones_complement(wrapped_total)
    return calculated_checksum

data = [7, 11, 12, 0, 6]
print(f"Given: {data}")

# Calculate checksum
checksum = calculate_checksum(data)

data_with_checksum = data + [checksum]

# Print the data with checksum
print("Data with checksum:", data_with_checksum)

# Verify checksum
calculated_checksum = verify_checksum(data_with_checksum)

# Print the result of checksum verification
print(f"Checksum: {calculated_checksum}")
print(f"Checksum valid: {True if not calculated_checksum else False}")
