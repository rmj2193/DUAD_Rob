time_seconds = int(input("Enter the time in seconds: "))
target = 600

if time_seconds < target:
    remaining = target - time_seconds
    print(f"{remaining} seconds left to reach 10 minutes.")
elif time_seconds > target:
    print("The time is greater than 10 minotes.")
else:
    print("The time is exactly 10 minutes.")