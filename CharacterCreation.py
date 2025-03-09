character_name = input("Tell us your name Adventurer: ").strip()

print(f"\nWelcome to Legacy, {character_name}!")

def character_race_menu():
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

    valid_races = {"Monk", "Paladin", "Sorcerer", "Blood Elf", "Human Barbarian", "???" }
    while True:
        race = input("Choose your race: ").strip().title()

        if race in valid_races:
            return race
        else:
            print("Please check your spelling and try again!")

character_race = character_race_menu()
print(f"\n{character_name} the almighty {character_race}.")
# chris is so flipping cool