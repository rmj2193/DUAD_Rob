try:
    name_input = input("Enter your name: ")

    #Validate that the name is not numeric
    if name_input.isdigit():
        raise ValueError("The name cannot be a number")

    #Ask for age and validate conversion
    try:
        age_input_text = input("Enter your age: ")
        age_value = int(age_input_text)
    except ValueError:
        print("Invalid number")
    else:
        print(f"Hello {name_input}, your age is {age_value}")

except ValueError as name_error:
    #If the name was numeric, show only the message
    print(str(name_error))