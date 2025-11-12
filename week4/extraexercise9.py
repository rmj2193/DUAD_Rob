numbers_to_read = 5
maximum_value = 0

for read_index in range(1, numbers_to_read + 1):
    input_value = float(input(f"Enter number #{read_index}: "))
    if maximum_value == 0 or input_value > maximum_value:
        maximum_value = input_value

print(f"The maximum of the {numbers_to_read} numbers is: {maximum_value}")