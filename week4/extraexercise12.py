numbers_to_check = 100
maximum_value = None

for number_index in range(1, numbers_to_check + 1):
    input_value = float(input(f"Enter number #{number_index}: "))
    if maximum_value is None or input_value > maximum_value:
        maximum_value = input_value
        
print(f"The maximum of the {numbers_to_check} numbers is: {maximum_value}")