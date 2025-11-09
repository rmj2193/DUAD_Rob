upper_limit = int(input("Enter an integer n (>= 1): "))
total_sum = 0
current_number = 1

while current_number <= upper_limit:
    total_sum += current_number
    current_number += 1
    
print(f"The sum 1..{upper_limit} is {total_sum}.")