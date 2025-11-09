import json

def load_data(filename):
    # Load the whole JSON file (expected top-level list)
    try:
        f = open(filename, "r", encoding="utf-8")
        content = f.read()
        f.close()
    except:
        print("Couldn't open 'jsonFile.json'. Make sure it exists.")
        raise SystemExit

    try:
        data = json.loads(content)
    except:
        print("Invalid JSON in 'jsonFile.json'.")
        raise SystemExit

    if not isinstance(data, list):
        print("Expected a top-level list of Pokémon.")
        raise SystemExit

    return data

def show_pokemons(pokemons):
    # Print each Pokémon: name (english), types, and Speed (as example attribute)
    if len(pokemons) == 0:
        print("No Pokémon found.")
        return

    print("=== Pokémon List ===")
    i = 0
    while i < len(pokemons):
        p = pokemons[i]

        # Name
        name = ""
        if isinstance(p, dict) and "name" in p and isinstance(p["name"], dict):
            name = str(p["name"].get("english", ""))

        # Types (list -> comma separated)
        types_str = ""
        if "type" in p and isinstance(p["type"], list):
            parts = []
            j = 0
            while j < len(p["type"]):
                t = str(p["type"][j]).strip()
                if t != "":
                    parts.append(t)
                j += 1
            types_str = ", ".join(parts)

        # Example attribute: Speed (dataset doesn't have "level")
        speed_str = ""
        if "base" in p and isinstance(p["base"], dict):
            spd = p["base"].get("Speed", "")
            if spd != "":
                speed_str = str(spd)

        print("Name: " + name + " | Types: " + types_str + " | Speed: " + speed_str)
        i += 1

def main():
    pokemons = load_data("jsonFile.json")
    show_pokemons(pokemons)

if __name__ == "__main__":
    main()