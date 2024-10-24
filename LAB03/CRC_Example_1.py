def crc_calculation(frame, generator):
    # Append zero bits to the frame
    frame += '0' * (len(generator) - 1)

    # Convert frame and generator to lists of bits
    frame_bits = list(map(int, frame))
    generator_bits = list(map(int, generator))

    # Perform polynomial division
    for i in range(len(frame_bits) - len(generator_bits) + 1):
        if frame_bits[i] == 1:
            for j in range(len(generator_bits)):
                frame_bits[i + j] ^= generator_bits[j]

    # Extract the remainder (CRC)
    remainder = ''.join(map(str, frame_bits[-(len(generator) - 1):]))

    return remainder

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
    print(f"Message after {len(generator) - 1} zero bits are appended: {frame + '0' * (len(generator) - 1)}")
    print(f"Remainder: {crc}")
    print(f"Transmitted Frame: {transmitted_frame}")

if __name__ == "__main__":
    main()
