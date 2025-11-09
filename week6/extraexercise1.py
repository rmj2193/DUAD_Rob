def count_char(text, character):
    #Count how many times the character appears in the text
    count = 0
    #Iterate over each symbol in the text
    for char in text:
        if char == character:
            count += 1
    return count

#Examples
print(count_char("Analyze this text for o appearances!", "o"))  