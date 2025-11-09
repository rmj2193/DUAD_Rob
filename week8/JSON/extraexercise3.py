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

def show_main_stats(pokemons):
    # For each pokémon, print its name and main base stats
    if len(pokemons) == 0:
        print("No Pokémon found.")
        return

    print("=== Pokémon Base Stats ===")
    i = 0
    while i < len(pokemons):
        p = pokemons[i]

        # Name
        name = ""
        if "name" in p and isinstance(p["name"], dict):
            name = str(p["name"].get("english", ""))

        # Base stats (handle missing keys gracefully)
        base = {}
        if "base" in p and isinstance(p["base"], dict):
            base = p["base"]

        hp = str(base.get("HP", ""))
        atk = str(base.get("Attack", ""))
        defe = str(base.get("Defense", ""))
        spa = str(base.get("Sp. Attack", ""))
        spd = str(base.get("Sp. Defense", ""))
        spe = str(base.get("Speed", ""))

        print(
            "Name: " + name +
            " | HP: " + hp +
            " | Attack: " + atk +
            " | Defense: " + defe +
            " | Sp. Attack: " + spa +
            " | Sp. Defense: " + spd +
            " | Speed: " + spe
        )
        i += 1

def main():
    filename = "jsonFile.json"  # defined here (no global)
    pokemons = load_data(filename)
    show_main_stats(pokemons)

if __name__ == "__main__":
    main()