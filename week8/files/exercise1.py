def read_input():
    # Open input file and collect non-empty lines
    try:
        f = open("text.txt", "r", encoding="utf-8")
        lines = f.readlines()
        f.close()
    except:
        print("Couldn't open 'text.txt'. Make sure it exists.")
        raise SystemExit

    songs = []
    for line in lines:
        name = line.strip()
        if name != "":
            songs.append(name)
    return songs

def sort_songs(songs):
    # Sort alphabetically ignoring uppercase/lowercase
    songs.sort(key=lambda s: s.lower())
    return songs

def write_output(songs):
    # Write sorted songs to output file
    try:
        f = open("salida.txt", "w", encoding="utf-8")
        for s in songs:
            f.write(s + "\n")
        f.close()
        print("Done: " + str(len(songs)) + " songs saved to 'salida.txt'.")
    except:
        print("Couldn't write to 'salida.txt'.")

def main():
    songs = read_input()
    songs = sort_songs(songs)
    write_output(songs)

if __name__ == "__main__":
    main()