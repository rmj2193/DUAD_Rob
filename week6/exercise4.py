def reverse_with_loop(text):
    #Build the reversed string manually by pre-pending each character
    result = ""
    for ch in text:
        result = ch + result  #put current char in front
    return result


#Examples
print(reverse_with_loop("Please Reverse This"))  