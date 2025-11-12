price = float(input("Enter the product price: "))

discount = price * (0.02 if price < 100 else 0.10)
final_price = price - discount

print(f"Discount applied: {discount:.2f}")
print(f"Final price: {final_price:.2f}")