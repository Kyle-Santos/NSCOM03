def ones_complement(n, bits):
    """Calculate the one's complement of a number."""
    return n ^ ((1 << bits) - 1)

def wrap_sum(sum_value):
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
    checksum = ones_complement(wrapped_sum, len(bin(wrapped_sum)[2:]))
    return checksum

def verify_checksum(data_with_checksum):
    """Verify the checksum for the given data."""
    checksum = data_with_checksum[-1]
    data = data_with_checksum[:-1]
    total = sum(data) + checksum
    wrapped_total = wrap_sum(total)
    calculated_checksum = ones_complement(wrapped_total, len(bin(wrapped_total)[2:]))
    return calculated_checksum

def main():
    # Example data
    data = "PKA_NSCOM03"
    decimal_values = [ord(char) for char in data]

    # Calculate checksum
    checksum = calculate_checksum(decimal_values)

    data_with_checksum = decimal_values + [checksum]

    calculated_checksum = verify_checksum(data_with_checksum)

    # Print results
    print(f"Given Text: {data}")
    print(f"Given Decimal Equivalent: {decimal_values}")
    print("Data with checksum: ", data_with_checksum)
    print(f"Checksum: {calculated_checksum}")
    print(f"Checksum valid: {True if not calculated_checksum else False}\n")

if __name__ == "__main__":
    main()
