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

def extract_level(pokemon):
    """
    Returns a numeric 'level' for a pokemon:
      1) If 'level' exists and is numeric -> use it.
      2) Else -> surrogate: average of base stats (HP, Attack, Defense, Sp. Attack, Sp. Defense, Speed).
      3) If neither available -> return None.
    """
    # Case 1: explicit 'level'
    if isinstance(pokemon, dict) and "level" in pokemon:
        lvl = pokemon["level"]
        if isinstance(lvl, (int, float)):
            return float(lvl)

    # Case 2: surrogate from base stats
    if "base" in pokemon and isinstance(pokemon["base"], dict):
        base = pokemon["base"]
        keys = ["HP", "Attack", "Defense", "Sp. Attack", "Sp. Defense", "Speed"]
        vals = []
        i = 0
        while i < len(keys):
            k = keys[i]
            v = base.get(k)
            if isinstance(v, (int, float)):
                vals.append(float(v))
            i += 1
        if len(vals) > 0:
            return sum(vals) / len(vals)

    # Case 3: no info
    return None

def group_levels_by_type(pokemons):
    """
    Builds a dict: { type_name: [levels...] }.
    Each pokemon contributes to each of its types.
    """
    type_levels = {}
    i = 0
    while i < len(pokemons):
        p = pokemons[i]
        lvl = extract_level(p)
        if lvl is not None and "type" in p and isinstance(p["type"], list):
            j = 0
            while j < len(p["type"]):
                t = p["type"][j]
                if isinstance(t, str):
                    key = t.strip()
                    if key != "":
                        if key not in type_levels:
                            type_levels[key] = []
                        type_levels[key].append(lvl)
                j += 1
        i += 1
    return type_levels

def compute_averages(type_levels):
    """
    Returns a sorted list of (type_name, avg_level, count) by type name (A->Z).
    """
    items = []
    for t in type_levels:
        levels = type_levels[t]
        if len(levels) > 0:
            avg = sum(levels) / len(levels)
            items.append((t, avg, len(levels)))
    # Sort alphabetically by type name (case-insensitive)
    items.sort(key=lambda x: x[0].lower())
    return items

def show_averages(items):
    # Print averages nicely
    if len(items) == 0:
        print("No types or levels found.")
        return

    print("=== Average Level per Type ===")
    i = 0
    while i < len(items):
        t, avg, cnt = items[i]
        # Print average with 2 decimals
        print(t + " -> avg level: " + "{:.2f}".format(avg) + " (n=" + str(cnt) + ")")
        i += 1

def main():
    filename = "jsonFile.json"  # defined here (no global)
    pokemons = load_data(filename)
    type_levels = group_levels_by_type(pokemons)
    items = compute_averages(type_levels)
    show_averages(items)

if __name__ == "__main__":
    main()