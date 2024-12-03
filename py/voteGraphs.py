import json
import matplotlib.pyplot as plt

def load_votes(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def plot_votes(votes_data):
    meals = {'Breakfast': [], 'Lunch': [], 'Dinner': []}
    products = list(votes_data.keys())

    for product, meals_data in votes_data.items():
        for meal, votes in meals_data.items():
            meals[meal].append(votes)

    fig, ax = plt.subplots(1, 3, figsize=(18, 6))
    for i, meal in enumerate(meals):
        ax[i].barh(products, meals[meal], color='skyblue')
        ax[i].set_title(f"{meal} Votes")
        ax[i].invert_yaxis()

    plt.tight_layout()
    plt.show()

def main():
    votes_data = load_votes('votes.txt')
    plot_votes(votes_data)

if __name__ == "__main__":
    main()
