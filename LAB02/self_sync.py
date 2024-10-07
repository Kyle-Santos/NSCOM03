# 4.2 Coding Signals: Self-Synchronization (Example 2)
def calculate_receiver_data_rate(data_rate):
    # Calculate the original data rate
    original_data_rate = data_rate

    # Calculate the receiver's data rate which is 0.1% faster
    receiver_data_rate = original_data_rate * 1.001

    # Calculate the extra bits per second received by the receiver
    extra_data = receiver_data_rate - original_data_rate

    # Format the output string
    output = f"At {original_data_rate} bps, the receiver receives {receiver_data_rate:.0f} bps instead of {original_data_rate} bps, {extra_data:.0f} extra bps"

    return output

# Example usage:
print(calculate_receiver_data_rate(1000))  # For 1 kbps
print(calculate_receiver_data_rate(1000000))  # For 1 Mbps