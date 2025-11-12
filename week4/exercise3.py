first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age in years: "))

if age < 0:
    category = "invalid age"
elif age <= 2:
    category = "baby"
elif age <= 9:
    category = "child"
elif age <= 12:
    category = "preadolescent"
elif age <= 17:
    category = "adolescent"
elif age <= 29:
    category = "young adult"
elif age <= 64:
    category = "adult"
else:
    category = "older adult"

print(f"{first_name} {last_name}, age {age}, is classified as a {category}.")