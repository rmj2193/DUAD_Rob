def print_case_counts(text):
    #Count uppercase and lowercase letters
    upper_count = 0
    lower_count = 0
    #Loop over each character
    for ch in text:
        #Check uppercase
        if ch.isupper():
            upper_count += 1
        #Check lowercase
        elif ch.islower():
            lower_count += 1
    #Print results
    print(f"Uppercase: {upper_count}")
    print(f"Lowercase: {lower_count}")

#Examples
print_case_counts("Hello There!")    