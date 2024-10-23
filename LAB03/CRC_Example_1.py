def crc_calculation(frame, generator):
    # Append 4 zero bits to the frame
    frame += '0' * 4

    # Convert frame and generator to integers
    frame_int = int(frame, 2)
    generator_int = int(generator, 2)

    # Perform polynomial division
    for i in range(len(frame) - 4):
        if frame_int & (1 << (len(frame) - 1)):
            frame_int ^= generator_int
        frame_int <<= 1

    # Extract the remainder (CRC)
    remainder = frame_int & ((1 << 4) - 1)

    # Convert remainder to binary string
    remainder_str = format(remainder, '04b')

    return remainder_str

def main():
    # Example frame and generator
    frame = "1101011011"
    generator = "10011"

    # Calculate CRC
    crc = crc_calculation(frame, generator)

    # Append the CRC to the original frame
    transmitted_frame = frame + crc

    print(f"Frame: {frame}")
    print(f"Generator: {generator}")
    print(f"Message after 4 zero bits are appended: {frame + '0' * 4}")
    print(f"Remainder: {crc}")
    print(f"Transmitted Frame: {transmitted_frame}")

if __name__ == "__main__":
    main()
