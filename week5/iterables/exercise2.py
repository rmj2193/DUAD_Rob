my_string = 'Pizza with pineapple'

#To start from the last character, we use len -1, we stop in -1 and the step is -1 to iterate backwards
for index in range(len(my_string) -1, -1, -1 ):
    print(my_string[index])