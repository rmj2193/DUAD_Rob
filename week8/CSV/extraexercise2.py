import csv

def read_rows(filename):
    # Open the CSV and read all rows with csv.reader()
    try:
        f = open(filename, "r", newline="", encoding="utf-8")
        reader = csv.reader(f)
        rows = list(reader)
        f.close()
    except:
        print("Couldn't open '" + filename + "'. Make sure it exists.")
        raise SystemExit
    return rows

def ask_esrb():
    # Ask the user for an ESRB rating (e.g., E, E10+, T, M, AO, RP)
    esrb = input("Enter ESRB rating to filter (e.g., E, E10+, T, M, AO, RP): ").strip().upper()
    if esrb == "":
        print("ESRB rating cannot be empty.")
        raise SystemExit
    return esrb

def filter_by_esrb(rows, esrb):
    # Assume first row is header: Name, Genre, Developer, ESRB
    matches = []
    i = 1
    while i < len(rows):
        row = rows[i]
        if len(row) >= 4:
            row_esrb = row[3].strip().upper()
            if row_esrb == esrb:
                matches.append(row)
        i += 1
    return matches

def show_matches(matches):
    # Print all matched games nicely
    if len(matches) == 0:
        print("No games found with that ESRB rating.")
        return

    print("\n=== Matches ===")
    i = 0
    while i < len(matches):
        row = matches[i]
        print("Name: " + row[0] +
              " | Genre: " + row[1] +
              " | Developer: " + row[2] +
              " | ESRB: " + row[3])
        i += 1
    print("Total matches: " + str(len(matches)))

def main():
    rows = read_rows("videojuegos.csv")
    esrb = ask_esrb()
    matches = filter_by_esrb(rows, esrb)
    show_matches(matches)

if __name__ == "__main__":
    main()