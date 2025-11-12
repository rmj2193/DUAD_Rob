import json

def load_data(filename):
    # Load the whole JSON file (expected top-level list of pokémon)
    try:
        f = open(filename, "r", encoding="utf-8")
        content = f.read()
        f.close()
    except:
        print("Couldn't open '" + filename + "'. Make sure it exists.")
        raise SystemExit

    try:
        data = json.loads(content)
    except:
        print("Invalid JSON in '" + filename + "'.")
        raise SystemExit

    if not isinstance(data, list):
        print("Expected a top-level list of Pokémon.")
        raise SystemExit

    return data

def ask_type():
    # Ask the user for a Pokémon type (e.g., Water, Fire, Electric)
    t = input("Enter a Pokémon type (e.g., Water): ").strip()
    if t == "":
        print("Type cannot be empty.")
        raise SystemExit
    return t

def filter_by_type(pokemons, type_name):
    # Return all pokémon whose 'type' list contains the given type (case-insensitive)
    matches = []
    key = type_name.lower()
    i = 0
    while i < len(pokemons):
        p = pokemons[i]
        if isinstance(p, dict) and "type" in p and isinstance(p["type"], list):
            j = 0
            found = False
            while j < len(p["type"]):
                t = str(p["type"][j]).strip().lower()
                if t == key:
                    found = True
                    break
                j += 1
            if found:
                matches.append(p)
        i += 1
    return matches

def show_matches(matches, type_name):
    # Print matched pokémon nicely: Name (english) and Types
    if len(matches) == 0:
        print("No Pokémon found for type: " + type_name)
        return

    print("\n=== Pokémon of type " + type_name + " ===")
    i = 0
    while i < len(matches):
        p = matches[i]

        # Name
        name = ""
        if "name" in p and isinstance(p["name"], dict):
            name = str(p["name"].get("english", ""))

        # Types string
        types_str = ""
        if "type" in p and isinstance(p["type"], list):
            parts = []
            k = 0
            while k < len(p["type"]):
                part = str(p["type"][k]).strip()
                if part != "":
                    parts.append(part)
                k += 1
            types_str = ", ".join(parts)

        print("Name: " + name + " | Types: " + types_str)
        i += 1

    print("Total matches: " + str(len(matches)))

def main():
    filename = "jsonFile.json"  # defined here (no global)
    pokemons = load_data(filename)
    type_name = ask_type()
    matches = filter_by_type(pokemons, type_name)
    show_matches(matches, type_name)

if __name__ == "__main__":
    main()