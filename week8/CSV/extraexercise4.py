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

def ask_developer():
    # Ask the user for a developer name (e.g., "Ubisoft")
    dev = input("Enter developer to filter (e.g., Ubisoft): ").strip()
    if dev == "":
        print("Developer name cannot be empty.")
        raise SystemExit
    return dev

def filter_by_developer(rows, developer_name):
    # Assume header: Name, Genre, Developer, ESRB  -> Developer index = 2
    # Compare case-insensitively
    matches = []
    dev_key = developer_name.lower()
    i = 1  # skip header
    while i < len(rows):
        row = rows[i]
        if len(row) >= 3:
            row_dev = row[2].strip().lower()
            if row_dev == dev_key:
                matches.append(row)
        i += 1
    return matches

def show_matches(matches, developer_name):
    # Print all matched games nicely
    if len(matches) == 0:
        print("No games found for developer: " + developer_name)
        return

    print("\n=== Games by " + developer_name + " ===")
    i = 0
    while i < len(matches):
        row = matches[i]
        # row: [Name, Genre, Developer, ESRB] (expected)
        name = row[0] if len(row) > 0 else ""
        genre = row[1] if len(row) > 1 else ""
        dev = row[2] if len(row) > 2 else ""
        esrb = row[3] if len(row) > 3 else ""
        print("Name: " + name +
              " | Genre: " + genre +
              " | Developer: " + dev +
              " | ESRB: " + esrb)
        i += 1
    print("Total matches: " + str(len(matches)))

def main():
    rows = read_rows("videojuegos.csv")
    developer_name = ask_developer()
    matches = filter_by_developer(rows, developer_name)
    show_matches(matches, developer_name)

if __name__ == "__main__":
    main()