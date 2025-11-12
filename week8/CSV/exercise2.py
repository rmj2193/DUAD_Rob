import csv

def collect_games():
    # Keep asking for games until Name is empty
    print("=== Video Games to TSV (tab-delimited) ===")
    print("Leave 'Name' empty to finish.\n")

    rows = []
    index = 1

    while True:
        print("Game #" + str(index))
        name = input("Name (Enter to finish): ").strip()
        if name == "":
            break  # finish input

        genre = input("Genre: ").strip()
        developer = input("Developer: ").strip()
        esrb = input("ESRB rating (e.g., E, E10+, T, M, AO, RP): ").strip()

        if genre == "" or developer == "" or esrb == "":
            print("All fields (Genre, Developer, ESRB) are required. Skipping this game.\n")
            continue

        rows.append([name, genre, developer, esrb])
        print("Added.\n")
        index += 1

    return rows

def write_tsv(filename, rows):
    # Write header + rows in TAB-delimited format
    try:
        # newline='' per csv docs to avoid extra blank lines on some platforms
        f = open(filename, "w", newline="", encoding="utf-8")
        # Use the built-in Excel TAB dialect
        writer = csv.writer(f, dialect="excel-tab")
        # (Alternative: writer = csv.writer(f, delimiter='\t'))
        writer.writerow(["Name", "Genre", "Developer", "ESRB"])
        writer.writerows(rows)
        f.close()
        print("\nDone: " + str(len(rows)) + " games saved to '" + filename + "'.")
    except:
        print("Couldn't write the TSV file.")

def main():
    rows = collect_games()
    write_tsv("videojuegos.tsv", rows)

if __name__ == "__main__":
    main()