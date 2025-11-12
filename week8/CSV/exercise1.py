import csv

def collect_games():
    # Keep asking for games until Name is empty
    print("=== Video Games to CSV ===")
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

def write_csv(filename, rows):
    # Write header + rows to CSV (UTF-8)
    try:
        f = open(filename, "w", newline="", encoding="utf-8")
        writer = csv.writer(f)
        writer.writerow(["Name", "Genre", "Developer", "ESRB"])
        for r in rows:
            writer.writerow(r)
        f.close()
        print("\nDone: " + str(len(rows)) + " games saved to '" + filename + "'.")
    except:
        print("Couldn't write the CSV file.")

def main():
    rows = collect_games()
    write_csv("videojuegos.csv", rows)

if __name__ == "__main__":
    main()