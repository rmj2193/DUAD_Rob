def sort_hyphen_words(text):
    #Split into words using hyphen
    raw_parts = text.split('-')
    #Trim spaces and drop empty parts using a regular for loop
    parts = []
    for p in raw_parts:
        cleaned = p.strip()
        if cleaned != '':
            parts.append(cleaned)
    #Sort alphabetically 
    parts.sort(key=str.lower)
    #Join-back-with-hyphen
    return '-'.join(parts)

#Examples
print(sort_hyphen_words("naranja-mora-piña"))   