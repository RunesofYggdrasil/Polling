import random
import json
import matplotlib.pyplot as plt

class Ingredient:
    def __init__(self, name, quantity, nutrition):
        self.name = name
        self.quantity = quantity
        self.nutrition = nutrition
    
    def __eq__(self, other):
        return self.name == other.name and self.quantity == other.quantity and self.nutrition == other.nutrition
    
    def __repr__(self):
        return f"{self.name} ({self.quantity}g): {self.nutrition}"

def randomize_nutrition():
    return {
        "calories": random.randint(5, 150),  
        "fats": {
            "total": random.randint(0, 10),  
            "saturated": random.randint(0, 5),  
            "trans": random.randint(0, 1), 
        },
        "cholesterol": random.randint(0, 30), 
        "sodium": random.randint(0, 200), 
        "carbohydrates": {
            "total": random.randint(1, 30), 
            "fibers": random.randint(0, 10), 
            "sugars": {
                "total": random.randint(0, 15), 
                "added": random.randint(0, 5), 
            },
        },
        "proteins": random.randint(1, 15),  
    }