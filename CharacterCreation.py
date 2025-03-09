def get_valid_races():
    return {
        "Monk",
        "Paladin",
        "Sorcerer",
        "Blood Elf",
        "Human Barbarian"
    }
def get_character_name(player_number):
    while True:
        player_name = input(f"Adventurer {player_number}, tell us your name: ").strip()

        if not player_name:
            print("Surely the Gods must have given you a name...")
        elif len(player_name) > 16:
            print("Our parchment only fits 16 characters...")
        else:
            return player_name
def display_race_menu():
    menu = r"""
        ┌────────────────────────────────────┐
        │          CHOOSE YOUR RACE          │
        ├────────────────────────────────────┤
        │ (+) Monk                           │
        │ (+) Paladin                        │
        │ (+) Sorcerer                       │
        │ (+) Blood Elf                      │
        │ (+) Human Barbarian                │
        └────────────────────────────────────┘
    """
    print(menu)
def character_race_menu(player_name):

    valid_races = get_valid_races()

    while True:
        character_race = input(f"{player_name}, choose your race: ").strip().title()

        if character_race in valid_races:
            return character_race
        else:
            print("I've not heard of this race before...")

while True:
    try:
        num_players = int(input("How many Adventurers are in your party?: ").strip())
        if 1 <= num_players <= 4:
            break
        else:
            print("Your party must consist of 1 to 4 Adventurers.")
    except ValueError:
        print("Sorry, I didn't catch that.")

players = [get_character_name(i + 1) for i in range(num_players)]

display_race_menu()

player_data = {player: character_race_menu(player) for player in players}

print(f"\nWelcome to Legacy:""\n")
for name, race in player_data.items():
    print(f"{name}, the mighty {race}!")
print("\nLet the adventuring begin!")
