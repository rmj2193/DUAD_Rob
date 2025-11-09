my_word_list = []
my_new_word_list = []

#Looping exactly 5 times
for index in range(1, 6):
    my_word_list.append(input('Please enter a word:'))

#Looping to extract words with len > 4
for index in range(len(my_word_list)):
    if(len(my_word_list[index]) > 4):
        my_new_word_list.append(my_word_list[index])

print(my_new_word_list)