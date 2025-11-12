def get_user_line():
    # Ask for a single line of text
    line = input("Enter a line of text: ")
    return line

def append_to_file(line):
    # Open the file in append mode and write the line with a newline
    try:
        f = open("salida2.txt", "a", encoding="utf-8")
        f.write(line + "\n")
        f.close()
        print("Done: line appended to 'salida2.txt'.")
    except:
        print("Couldn't write to 'salida2.txt'.")

def main():
    user_line = get_user_line()
    append_to_file(user_line)

if __name__ == "__main__":
    main()