def read_input_lines():
    # Open input file and read all lines
    try:
        f = open("text.txt", "r", encoding="utf-8")
        lines = f.readlines()
        f.close()
    except:
        print("Couldn't open 'text.txt'. Make sure it exists.")
        raise SystemExit
    return lines

def to_uppercase(lines):
    # Convert each line to uppercase (preserving line breaks later)
    upper_lines = []
    for line in lines:
        # remove trailing newline(s) before uppercasing
        cleaned = line.replace("\r", "").replace("\n", "")
        upper_lines.append(cleaned.upper())
    return upper_lines

def write_output_lines(lines):
    # Write each uppercased line to 'salida.txt' with newline
    try:
        f = open("salida.txt", "w", encoding="utf-8")
        for line in lines:
            f.write(line + "\n")
        f.close()
        print("Done: " + str(len(lines)) + " lines written to 'salida.txt'.")
    except:
        print("Couldn't write to 'salida.txt'.")

def main():
    lines = read_input_lines()
    upper_lines = to_uppercase(lines)
    write_output_lines(upper_lines)

if __name__ == "__main__":
    main()