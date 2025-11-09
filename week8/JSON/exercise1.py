import json


def load_data(filename):
    # Load existing data from jsonFile.json (expecting a top-level list)
    try:
        f = open(filename, "r", encoding="utf-8")
        content = f.read().strip()
        f.close()
        if content == "":
            return []
        data = json.loads(content)
        if isinstance(data, list):
            return data
        else:
            # If the structure isn't a list, start fresh
            return []
    except:
        # If file doesn't exist or invalid JSON, start fresh
        return []

def ask_new_pokemon():
    # Ask user for the Pokémon info following the provided structure
    print("=== Add New Pokémon (matching lesson format) ===")
    name_en = input("Name (english): ").strip()
    types_raw = input("Types (comma-separated, e.g., Fire, Flying): ").strip()

    # Basic required fields
    if name_en == "" or types_raw == "":
        print("Name and Types cannot be empty.")
        raise SystemExit

    # Build the types list from comma-separated input
    parts = types_raw.split(",")
    types_list = []
    for p in parts:
        t = p.strip()
        if t != "":
            types_list.append(t)

    if len(types_list) == 0:
        print("Types list cannot be empty.")
        raise SystemExit

    # Base stats (integers)
    hp_txt = input("HP (integer): ").strip()
    atk_txt = input("Attack (integer): ").strip()
    def_txt = input("Defense (integer): ").strip()
    spa_txt = input("Sp. Attack (integer): ").strip()
    spd_txt = input("Sp. Defense (integer): ").strip()
    spe_txt = input("Speed (integer): ").strip()

    try:
        hp = int(hp_txt)
        atk = int(atk_txt)
        defense = int(def_txt)
        sp_attack = int(spa_txt)
        sp_defense = int(spd_txt)
        speed = int(spe_txt)
    except:
        print("All base stats must be integers.")
        raise SystemExit

    # Construct the Pokémon object exactly like the given format
    new_pokemon = {
        "name": {
            "english": name_en
        },
        "type": types_list,
        "base": {
            "HP": hp,
            "Attack": atk,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }
    return new_pokemon

def save_data(pokemon_list, filename):
    # Save the full list back to jsonFile.json with pretty formatting
    try:
        f = open(filename, "w", encoding="utf-8")
        json.dump(pokemon_list, f, ensure_ascii=False, indent=2)
        f.close()
        print("Done: Pokémon added and saved to '" + filename + "'.")
    except:
        print("Couldn't write to '" + filename + "'.")

def main():
    data = load_data("jsonFile.json")
    new_pokemon = ask_new_pokemon()
    data.append(new_pokemon)
    save_data(data, "jsonFile.json")

if __name__ == "__main__":
    main()