import csv

def read_csv_rows():
    # Open the CSV file and read rows using csv.reader
    try:
        f = open("videojuegos.csv", "r", encoding="utf-8", newline="")
        reader = csv.reader(f)
        rows = []
        for row in reader:
            rows.append(row)
        f.close()
        return rows
    except:
        print("Couldn't open 'videojuegos.csv'. Make sure it exists.")
        raise SystemExit

def display_rows(rows):
    # Show rows in a readable format
    if len(rows) == 0:
        print("No data found in 'videojuegos.csv'.")
        return

    # Assume first row is the header (Name, Genre, Developer, ESRB)
    header = rows[0]
    data = rows[1:] if len(rows) > 1 else []

    if len(data) == 0:
        print("File contains only the header.")
        return

    index = 1
    for row in data:
        # Safely access columns
        name = row[0] if len(row) > 0 else ""
        genre = row[1] if len(row) > 1 else ""
        developer = row[2] if len(row) > 2 else ""
        esrb = row[3] if len(row) > 3 else ""

        print("Game #" + str(index))
        print("  Name: " + name)
        print("  Genre: " + genre)
        print("  Developer: " + developer)
        print("  ESRB: " + esrb)
        print("-" * 40)
        index += 1

def main():
    rows = read_csv_rows()
    display_rows(rows)

if __name__ == "__main__":
    main()