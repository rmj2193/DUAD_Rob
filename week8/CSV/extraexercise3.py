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

def count_by_genre(rows):
    # Counts how many games per genre (case-insensitive grouping)
    # Assumes header: Name, Genre, Developer, ESRB  -> Genre index = 1
    counts = {}       # key: lowercase genre, value: count
    display_name = {} # key: lowercase genre, value: first seen display text

    i = 1  # skip header at index 0
    while i < len(rows):
        row = rows[i]
        if len(row) >= 2:
            genre = row[1].strip()
            if genre != "":
                key = genre.lower()
                if key not in counts:
                    counts[key] = 0
                    display_name[key] = genre
                counts[key] = counts[key] + 1
        i += 1

    return counts, display_name

def sort_counts(counts, display_name):
    # Returns a list of (genre_display, count) sorted by genre name A->Z
    items = []
    for key in counts:
        items.append((display_name[key], counts[key]))
    # Simple alphabetical order by display text
    items.sort(key=lambda x: x[0].lower())
    return items

def show_counts(sorted_items):
    # Print the result nicely
    if len(sorted_items) == 0:
        print("No genres found.")
        return

    print("=== Games per Genre ===")
    total = 0
    for genre, cnt in sorted_items:
        print(genre + ": " + str(cnt))
        total += cnt
    print("Total games counted: " + str(total))

def main():
    rows = read_rows("videojuegos.csv")
    counts, display_name = count_by_genre(rows)
    sorted_items = sort_counts(counts, display_name)
    show_counts(sorted_items)

if __name__ == "__main__":
    main()