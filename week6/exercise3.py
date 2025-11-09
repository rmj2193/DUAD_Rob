def sum_list(numbers):
    #Return the sum of all numbers in the list
    total = 0
    for n in numbers:
        total += n
    return total

#Examples
print(sum_list([1, 2, 3, 4]))    