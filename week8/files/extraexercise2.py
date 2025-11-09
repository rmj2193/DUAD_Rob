def read_input():
    # Read the whole file as a single string
    try:
        f = open("text.txt", "r", encoding="utf-8")
        content = f.read()
        f.close()
    except:
        print("Couldn't open 'text.txt'. Make sure it exists.")
        raise SystemExit
    return content

def count_words(text):
    # Split on any whitespace (spaces, newlines, tabs) and count
    words = text.split()
    return len(words)

def show_output(total):
    # Print the number of words to the console
    print("This file contains " + str(total) + " words")

def main():
    text = read_input()
    total = count_words(text)
    show_output(total)

if __name__ == "__main__":
    main()