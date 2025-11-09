def count_vowels(text):
    #Define the set of vowels including accents
    vowels = "AEIOUÁÉÍÓÚÜaeiouáéíóúü"
    #Start the counter at zero
    count = 0
    #Go through each character in the text
    for char in text:
        #If the character is a vowel add one
        if char in vowels:
            count += 1
    #Return the total number of vowels
    return count

#Examples
print(count_vowels("Please check this test for vowels!"))      