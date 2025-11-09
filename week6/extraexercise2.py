def filter_long_words(words, n):
    #Return a new list with words longer than n
    result = []
    #Go through each word in the list
    for word in words:
        #If the word length is greater than n, keep it
        if len(word) > n:
            result.append(word)
    #Return the final filtered list
    return result

#Examples
print(filter_long_words(["Hello", "Fantastic", "Robster", "Guitar", "Brother"], 5))