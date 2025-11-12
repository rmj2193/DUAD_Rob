def sum_values(values_list):
    #Sum every element that can be converted to float and report progress
    total_sum = 0.0

    for element_value in values_list:
        try:
            numeric_value = float(element_value)
            total_sum += numeric_value
            print(f"{numeric_value} \"added successfully\"")
        except ValueError:
            print(f"Invalid element: {element_value}")

    print("\"Total sum:\"", total_sum)