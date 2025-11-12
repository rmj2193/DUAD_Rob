#make the max number minus infinite to be able to accept negative numbers and floats
max_num = float('-inf')
my_num_list = []

#iterate exactly 10 times
for index in range(1, 11):
    my_number = float(input('Please enter a number:'))
    my_num_list.append(my_number)
    if(my_number > max_num):
        max_num = my_number

print(f'{my_num_list} The highest number was: {max_num}')