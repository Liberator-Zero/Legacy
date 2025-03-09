def get_valid_races():
    return {"Monk", "Paladin", "Sorcerer", "Blood Elf", "Human Barbarian"}
def get_valid_attributes():
    return {"Strength", "Dexterity", "Intelligence", "Constitution", "Wisdom", "Charisma", "Luck"}
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
    display_race_menu()

    while True:
        character_race = input(f"{player_name}, choose your race: ").strip().title()
        if character_race in valid_races:
            return character_race
        else:
            print("I've not heard of this race before...")
def display_attribute_menu():
    menu = r"""
        ┌────────────────────────────────────┐
        │       CHOOSE YOUR ATTRIBUTES       │
        ├────────────────────────────────────┤
        │ (+) Strength                       │
        │ (+) Dexterity                      │
        │ (+) Intelligence                   │
        │ (+) Constitution                   │
        │ (+) Wisdom                         │
        │ (+) Charisma                       │
        │ (+) Luck                           │
        └────────────────────────────────────┘
    """
    print(menu)
def character_attribute_menu(player_name):
    valid_attributes = get_valid_attributes()
    display_attribute_menu()

    print(f"\n{player_name}, tell me where your true strength lies...")

    while True:
        major_attribute = input("What is your greatest strength? ").strip().title()
        if major_attribute in valid_attributes:
            break
        else:
            print("I've not heard of such talents... Choose from:", ", ".join(valid_attributes))

    chosen_minor_attributes = []
    print("\nNow, select two other talents that support your journey.")

    while len(chosen_minor_attributes) < 2:
        minor_attribute = input(f"What is your {('first', 'second')[len(chosen_minor_attributes)]} minor attribute? ").strip().title()
        if minor_attribute not in valid_attributes:
            print("That skill is unknown to me...")
        elif minor_attribute == major_attribute or minor_attribute in chosen_minor_attributes:
            print("You have already chosen this attribute! Pick another.")
        else:
            chosen_minor_attributes.append(minor_attribute)

    return major_attribute, tuple(chosen_minor_attributes)

num_players = int(input("How many Adventurers are in your party?: ").strip())
players = [get_character_name(i + 1) for i in range(num_players)]

player_data = {player: {"Race": character_race_menu(player), "Attributes": character_attribute_menu(player)} for player in players}

print("\nWelcome to Legacy:")
for name, info in player_data.items():
    print(f"{name}, the mighty {info['Race']}!")
print("\nLet the adventuring begin!")
