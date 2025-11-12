my_list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#Iterate backwards since the pop was giving me issues with regular iteration
for index in range(len(my_list2)-1, -1, -1):
    if(my_list2[index]%2 != 0):
        my_list2.pop(index)

print(my_list2)