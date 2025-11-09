numbers_to_sum = 100
total_sum = 0.0

for number_index in range(1, numbers_to_sum + 1):
    input_value = float(input(f"Enter number #{number_index}: "))
    total_sum += input_value

print(f"The sum of the {numbers_to_sum} numbers is: {total_sum}")