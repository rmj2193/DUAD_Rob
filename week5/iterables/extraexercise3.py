#make the min number infinite to be able to accept negative numbers and floats
min_num = float('inf')
my_num_list2 = [-1000,0,2,65,-100,500,-900]

for index in range(len(my_num_list2)):
    if(my_num_list2[index] < min_num):
        min_num = my_num_list2[index]

print(f'The lowest number was: {min_num}')