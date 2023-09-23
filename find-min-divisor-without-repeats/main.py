def find_min_divisor_without_repeats(arr):
    divisor = 2

    while True:
        remainders = set()
        for num in arr:
            remainder = num % divisor
            if remainder in remainders:
                break
            remainders.add(remainder)
        else:
            return divisor  # If no remainders repeated, return the divisor

        divisor += 1  # If remainders repeated, increment the divisor and try again


# Example usage:
unique_array = [0x50, 0x11, 0x92, 0xD3, 0x20, 0x61, 0xE2, 0xA3, 0x64, 0x25,
                0xA6, 0xE7, 0xA8, 0xE9, 0x6A, 0x2B, 0xEC, 0xAD, 0x2E, 0x47, 0x49, 0x3C, 0x7D]
min_divisor = find_min_divisor_without_repeats(unique_array)
print("Minimum divisor:", min_divisor)
