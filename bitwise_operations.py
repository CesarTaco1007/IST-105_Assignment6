import sys

def validate_input(input_string):
    try:
        return [int(x.strip()) for x in input_string.split(',')]
    except ValueError:
        print("Error: Input must be integers separated by commas")
        sys.exit(1)

def perform_bitwise_operations(numbers):
    if not numbers:
        return 0, 0, 0
    result_and = numbers[0]
    result_or = numbers[0]
    result_xor = numbers[0]
    for num in numbers[1:]:
        result_and &= num
        result_or |= num
        result_xor ^= num
    return result_and, result_or, result_xor

def filter_numbers(numbers, threshold):
    return [num for num in numbers if num > threshold]

def main():
    # Assuming input is passed as a command-line argument
    if len(sys.argv) < 3:
        print("Usage: python bitwise_operations.py <comma_separated_numbers> <threshold>")
        sys.exit(1)

    input_string = sys.argv[1]
    threshold = int(sys.argv[2])

    numbers = validate_input(input_string)
    and_result, or_result, xor_result = perform_bitwise_operations(numbers)
    filtered_numbers = filter_numbers(numbers, threshold)

    print(f"Bitwise AND: {and_result}")
    print(f"Bitwise OR: {or_result}")
    print(f"Bitwise XOR: {xor_result}")
    print(f"Numbers greater than threshold: {filtered_numbers}")

if __name__ == "__main__":
    main()