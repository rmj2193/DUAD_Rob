def add(first_number, second_number):
    #Return the sum of two numbers
    return first_number + second_number


def subtract(first_number, second_number):
    #Return the difference of two numbers
    return first_number - second_number


def multiply(first_number, second_number):
    #Return the product of two numbers
    return first_number * second_number


def divide(first_number, second_number):
    #Divide and validate division by zero
    if second_number == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return first_number / second_number


def read_number(prompt_text):
    #Read a number from the user and validate it
    user_input = input(prompt_text).strip()
    try:
        #Return the parsed number and no error message
        return float(user_input), None
    except ValueError:
        #Return no value and an error message
        return None, "Invalid number. Please enter a valid numeric value."


def print_menu(current_number):
    #Show the menu and the current number
    print("\n--------------------------")
    print(f"Current number: {current_number}")
    print("Choose an option:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear result set to 0")
    print("0. Quit")
    print("--------------------------")


def main():
    #Main loop to run the calculator
    current_number = 0.0
    while True:
        #Show the menu and ask for an option
        print_menu(current_number)
        selected_option = input("Enter option 0 to 5: ").strip()

        #Handle exit
        if selected_option == "0":
            print("Goodbye!")
            break

        #Validate menu option
        if selected_option not in {"1", "2", "3", "4", "5"}:
            print("Error: Invalid option. Please choose a number between 0 and 5.")
            continue

        #Handle clear result
        if selected_option == "5":
            current_number = 0.0
            print(f"Result cleared. Current number is now {current_number}.")
            continue

        #For arithmetic options ask for the second number
        second_number, error_message = read_number("Enter the number to use in the operation: ")
        if error_message is not None:
            print(f"Error: {error_message}")
            continue

        #Perform the selected operation
        if selected_option == "1":
            current_number = add(current_number, second_number)
            print(f"Added. New current number: {current_number}")
        elif selected_option == "2":
            current_number = subtract(current_number, second_number)
            print(f"Subtracted. New current number: {current_number}")
        elif selected_option == "3":
            current_number = multiply(current_number, second_number)
            print(f"Multiplied. New current number: {current_number}")
        elif selected_option == "4":
            try:
                current_number = divide(current_number, second_number)
                print(f"Divided. New current number: {current_number}")
            except ZeroDivisionError as error:
                print(f"Error: {error}")
                continue



if __name__ == "__main__":
    main()