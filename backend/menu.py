import json
"""
~ Shamar
"""
def load_menu(menu_file):
    try:
        with open(menu_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if menu file is not found
