def print_formatted(number):
    width = len(bin(number)) - 2

    for i in range(1, number + 1):
        # Convert number to different bases
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")

# Example usage:
number = 170
print_formatted(number)
