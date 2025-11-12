number = int(input("Enter a number from 1 to 10: "))

print(f"\nMultiplication table for {number} (1 to 12):")

for multiplier in range(1, 13):
    product = number * multiplier
    print(f"{number} x {multiplier:2} = {product}")