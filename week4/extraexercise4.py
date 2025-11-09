first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if first_number < second_number:
    first_number, second_number = second_number, first_number

print(f"A={first_number}, B={second_number}")