def crc32(frame, generator):
    # Convert frame and generator to integers
    frame_int = int(frame, 2)
    generator_int = int(generator, 2)

    # Append 32 zero bits to the frame
    frame_int <<= 32

    # Perform polynomial division
    for i in range(frame_int.bit_length() - 1, -1, -1):
        if frame_int & (1 << (i + 32 - 1)):
            frame_int ^= generator_int << (i)

    # Extract the remainder (CRC-32 checksum)
    remainder = frame_int & ((1 << 32) - 1)

    # Convert remainder to binary string
    remainder_str = format(remainder, '032b')

    return remainder_str

def main():
    # Example frame and generator
    frame = "1101011011"
    generator = "100000100110000010001110110110111"

    # Calculate CRC-32 checksum
    crc_checksum = crc32(frame, generator)

    # Append the checksum to the original frame
    transmitted_frame = frame + crc_checksum

    print(f"Original Frame: {frame}")
    print(f"Generator: {generator}")
    print(f"CRC-32 Checksum: {crc_checksum}")
    print(f"Transmitted Frame: {transmitted_frame}")


main()
