my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#save the fist and last to later switch
first = my_list[0]
last = my_list[len(my_list)-1]

#Switching fist for last
my_list.pop(0)
my_list.insert(0, last)

#Switchin last for first
my_list.pop(len(my_list)-1)
my_list.insert(len(my_list), first)

print(my_list)