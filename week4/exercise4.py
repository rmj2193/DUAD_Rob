import random

secret = random.randint(1, 10)
attempts = 0

print("Guess the secret number between 1 and 10.")

while True:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess < secret:
        print("Higher...")
    elif guess > secret:
        print("Lower...")
    else:
        print(f"Correct! It was {secret}. Attempts: {attempts}")
        break