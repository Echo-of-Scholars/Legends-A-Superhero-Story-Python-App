import json

def save_character(character, filename):
    with open(filename, "w") as file:
        json.dump(character.__dict__, file, indent=4)

def load_character(filename):
    with open(filename, "r") as file:
        character = Character()
        character_dict = json.load(file)
        for key, value in character_dict.items():
            setattr(character, key, value)
        return character