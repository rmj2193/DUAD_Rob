def is_prime(number):
    #Handle small cases
    if number <= 1:
        return False
    if number == 2:
        return True
    #Even numbers greater than two are not prime
    if number % 2 == 0:
        return False
    #Check odd divisors up to square root of the number
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def filter_primes(numbers):
    #Return a new list containing only prime numbers
    prime_numbers = []
    for candidate in numbers:
        if is_prime(candidate):
            prime_numbers.append(candidate)
    return prime_numbers

#Examples
print(filter_primes([1, 4, 6, 7, 13, 9, 67]))  