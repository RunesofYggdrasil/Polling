import json

def load_votes(votes_file):
    """
    Loads the votes from a JSON file, returning an empty dictionary if the file is not found.
    """
    try:
        with open(votes_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def record_vote(menu_item_name, meal_type, votes_file):
    """
    Records a vote for a menu item and meal type, updating the votes file.
    """
    votes = load_votes(votes_file)

    if menu_item_name not in votes:
        votes[menu_item_name] = {"Breakfast": 0, "Lunch": 0, "Dinner": 0}

    if meal_type in votes[menu_item_name]:
        votes[menu_item_name][meal_type] += 1

    with open(votes_file, 'w') as file:
        json.dump(votes, file, indent=4)
