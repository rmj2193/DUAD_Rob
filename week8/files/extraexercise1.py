def read_input():
    # Open input file and read all lines
    try:
        f = open("text.txt", "r", encoding="utf-8")
        lines = f.readlines()
        f.close()
    except:
        print("Couldn't open 'text.txt'. Make sure it exists.")
        raise SystemExit
    return lines

def join_into_single_line(lines):
    # Remove newline characters and join into a single line (no extra spaces)
    single_line = ""
    for line in lines:
        # Remove '\n' and also '\r' just in case
        cleaned = line.replace("\n", "").replace("\r", "")
        single_line += cleaned + " "
    return single_line

def write_output(text):
    # Write the single-line text into the output file
    try:
        f = open("salida.txt", "w", encoding="utf-8")
        f.write(text)  # no trailing newline, stays as one line
        f.close()
        print("Done: content saved as a single line in 'salida.txt'.")
    except:
        print("Couldn't write to 'salida.txt'.")

def main():
    lines = read_input()
    single_line_text = join_into_single_line(lines)
    write_output(single_line_text)

if __name__ == "__main__":
    main()