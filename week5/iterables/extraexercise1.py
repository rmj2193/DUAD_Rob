my_list_input = input('Please enter a number list surrounded by []:')
number_to_find = input('Please enter the number you want to find in the list:')
hit_times = 0

#Looping for amount of number hits
for index in range(len(my_list_input)-1):
    if(number_to_find == my_list_input[index]):
        hit_times = hit_times +1

if(hit_times == 0):
    print('Number not found in list')
else:
    print(f'The number {number_to_find} was found {hit_times} times')