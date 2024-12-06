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

def submit_vote(votes_file, meal, menu_item_name):
    """
    Records a vote for a menu item and meal type, updating the meals file.
    """
    meals = load_votes(votes_file)
    meal_type = meal.lower()

    meal_names = [choice["fields"]["choice_text"] for choice in meals["choices"][meal_type]]

    if menu_item_name not in meal_names:
        meals["choices"][meal_type].append({"model": "polls.choice", "meal": meal, "pk": meals["choices"][meal_type][-1]["pk"] + 1, "fields": {"question": meals["choices"][meal_type][-1]["fields"]["question"], "choice_text": menu_item_name, "votes": 1}})
    else:
        menu_index = meal_names.index(menu_item_name)
        meals["choices"][meal_type][menu_index]["fields"]["votes"] += 1
        

    with open(votes_file, 'w') as file:
        json.dump(meals, file, indent=4)