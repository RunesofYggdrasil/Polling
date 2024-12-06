from flask import Flask, render_template, request, redirect, url_for, jsonify
from menu import load_menu
from votes import record_vote, submit_vote, load_votes
from description import get_description
import os
from graph import plot_votes

BASE_DIR = os.path.dirname(__file__)
MENU_FILE = os.path.join(BASE_DIR, "data", "menu.json")
VOTES_FILE = os.path.join(BASE_DIR, "data", "votes.json")
MEALS_FILE = os.path.join(BASE_DIR, "data", "meals.json")

app = Flask(__name__)

MENU_FILE = "data/menu.json"
VOTES_FILE = "data/votes.json"

@app.route('/')
def index():
   menu_items = load_menu(MENU_FILE)
   graph_path = plot_votes(load_votes(VOTES_FILE))
   return render_template('primary.html', menu_items=menu_items, graph_path=graph_path)

@app.route('/vote', methods=['POST'])
def vote():
   selected_meal = request.form.get('menu_item')
   meal_type = request.form.get('meal_type')
   if selected_meal and meal_type:
       record_vote(selected_meal, meal_type, VOTES_FILE)
   return redirect(url_for('results'))

@app.route('/results')
def results():
   votes = load_votes(VOTES_FILE)
   graph_path = plot_votes(votes)
   return render_template('results.html', votes=votes, graph_path=graph_path)

@app.route('/vote-new', methods=['POST'])
def vote_new():
   meal = request.form.get('meal_type')
   menu_item = request.form.get('menu_item')
   if meal and menu_item:
      submit_vote(MEALS_FILE, meal, menu_item)
   return redirect(url_for('results'))

@app.route('/description', methods=['POST'])
def description():
   menu_item = request.json.get('menu_item')
   if menu_item:
       description = get_description(menu_item)
       return jsonify({'description': description})
   return jsonify({'description': 'No description available.'}), 400

if __name__ == "__main__":
   app.run(debug=True)