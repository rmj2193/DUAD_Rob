#Importing ast library to be able to convert the input string list into a real number list
import ast

#Receiving input list, converting it to number list
my_list_input2 = input('Please enter a number list surrounded by []:')
my_list_input2 = ast.literal_eval(my_list_input2)
my_new_list = []
total_sum = 0

#Loop to sum total 
for index in range(len(my_list_input2)):
    total_sum = total_sum + my_list_input2[index]

#Calculating average
average = total_sum / len(my_list_input2)

#Looping again to create list with numbers higher than avg
for index in range(len(my_list_input2)):
    if(my_list_input2[index] > average):
        my_new_list.append(my_list_input2[index])

#Using :.2f to use only two decimals and keeping it clean for visiblity
print(f'The average is: {average:.2f} and the New list is {my_new_list}')