my_positive_list = [1,2,3,4,5,6,7,2,-3]

for index in range(len(my_positive_list)):
    if(my_positive_list[index] < 0):
        #Breaking to exit loop when we get a hit
        print('There is at least one negative number on the list')
        break
#Putting else outside the loop to avoid line repetition
else:
    print('All numbers in the list are positive')