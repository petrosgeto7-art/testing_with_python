"""
Input an integer and number of shift positions.

Show results of left shift and right shift.

Print the binary form before and after.
"""
def shift_operations(num, shift_positions):
    # Binary representation before shifting
    binary_before = bin(num)[2:]
    
    # Left shift
    left_shifted = num << shift_positions
    binary_left_shifted = bin(left_shifted)[2:]

    # Right shift
    right_shifted = num >> shift_positions
    binary_right_shifted = bin(right_shifted)[2:]

    # Print results
    print(f"Original number: {num}")
    print(f"Binary before shift: {binary_before}")
    print(f"Left shift ({shift_positions} positions): {left_shifted}")
    print(f"Binary after left shift: {binary_left_shifted}")
    print(f"Right shift ({shift_positions} positions): {right_shifted}")
    print(f"Binary after right shift: {binary_right_shifted}")

# Example usage
num = int(input("Enter an integer: "))
shift_positions = int(input("Enter number of shift positions: "))
shift_operations(num, shift_positions)
