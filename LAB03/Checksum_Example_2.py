import socket
import struct

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

def sender(data, host='localhost', port=12345):
    # Calculate checksum
    decimal_values = [ord(char) for char in data]
    checksum = calculate_checksum(decimal_values)
    data_with_checksum = decimal_values + [checksum]

    # Create a socket and connect to the receiver
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Sender: Connected to receiver")

        # Send data with checksum
        packed_data = struct.pack(f'{len(data_with_checksum)}B', *data_with_checksum)
        s.sendall(packed_data)
        print("Sender: Data sent")

def receiver(host='localhost', port=12345):
    # Create a socket and bind to the address
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Receiver: Listening for connections")

        conn, addr = s.accept()
        with conn:
            print(f"Receiver: Connected by {addr}")
            data = conn.recv(1024)
            unpacked_data = list(struct.unpack(f'{len(data)}B', data))
            print(f"Receiver: Received data: {unpacked_data}")

            # Verify checksum
            calculated_checksum = verify_checksum(unpacked_data)
            print(f"Receiver: Calculated checksum: {calculated_checksum}")
            print(f"Receiver: Checksum valid: {True if not calculated_checksum else False}")

if __name__ == "__main__":
    data = "PKA_NSCOM03"
    print(f"Given Text: {data}")

    # Start the receiver in a separate thread or process
    import threading
    receiver_thread = threading.Thread(target=receiver)
    receiver_thread.start()

    # Start the sender
    sender(data)

    # Wait for the receiver thread to finish
    receiver_thread.join()
