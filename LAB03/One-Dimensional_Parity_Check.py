from tabulate import tabulate

def calculate_parity(data, parity_type='even'):
    parity_bit = 0
    for bit in data:
        parity_bit ^= int(bit)

    if parity_type == 'even':
        return '1' if parity_bit == 1 else '0'
    elif parity_type == 'odd':
        return '0' if parity_bit == 1 else '1'

def main():
    # Example data
    data = "1101011011"

    # Calculate even parity
    even_parity = calculate_parity(data, 'even')

    # Calculate odd parity
    odd_parity = calculate_parity(data, 'odd')

    # Prepare data for table
    table_data = [
        ["Data", data],
        ["Even Parity Bit", even_parity],
        ["Odd Parity Bit", odd_parity]
    ]

    # Print table
    print(tabulate(table_data, headers=["Description", "Value"], tablefmt="grid"))

if __name__ == "__main__":
    main()
