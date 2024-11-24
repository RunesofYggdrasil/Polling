class Ingredient:
    """ 
    A class to represent an ingredient of a meal.

        Attributes:
            self.name (str): The name of the ingredient.
            self.serving_size (int): The serving size of the Ingredient which the nutritional values apply to.
            self.nutritional_content (int dict): The integer values of various nutritional aspects of the ingredient in the appropriate measuring systems. The dictionary should include the following:
                calories: int
                fats:
                    total: int
                    saturated: int
                    trans: int
                cholesterol: int
                sodium: int
                carbohydrates:
                    total: int
                    fibers: int
                    sugars:
                        total: int
                        added: int
                proteins: int

        Methods:
            get_name() (-> str): Returns the name of the Ingredient.
            get_serving_size() (-> str): Returns the serving size of the Ingredient.
            get_nutritional_content() (-> int dict): Returns the nutritional content of the Ingredient.
            get_key_list() (-> str list): Returns a list of all the possible keys in the nutritional content dictionary.
            get_at_key(str list) (-> int dict or int): Returns the value of the dictionary at a key or list of keys.
    """

    def __init__(self, init_name: str, init_serving_size: int, init_nutritional_content: dict):
        """ 
        Initializes an Ingredient.
        
            Parameters:
                init_name (str): The name of the ingredient.
                init_serving_size (int): The serving size of the Ingredient which the nutritional values apply to.
                init_nutritional_content (int dict): The integer values of various nutritional aspects of the ingredient in the appropriate measuring systems. The dictionary should include the following: {calories: int, fats: {total: int, saturated: int, trans: int}, cholesterol: int, sodium: int, carbohydrates: {total: int, fibers: int, sugars: {total: int, added: int}}, proteins: int}
        """
        self.name = init_name
        self.serving_size = init_serving_size
        self.nutritional_content = init_nutritional_content

    def __str__(self):
        """ Returns a string representation of the Ingredient. """
        # The string is split up into variables for readability.
        title_lines = self.name + "\nServing Size: " + str(self.serving_size) + "\n" + "Calories: " + str(self.nutritional_content["calories"])
        fats_lines = "\nTotal Fats: " + str(self.nutritional_content["fats"]["total"]) + "\n\tSaturated Fats: " + str(self.nutritional_content["fats"]["saturated"]) + "\n\tTrans Fats: " + str(self.nutritional_content["fats"]["trans"])
        other_lines = "\nCholesterol: " + str(self.nutritional_content["cholesterol"]) + "\nSodium: " + str(self.nutritional_content["sodium"]) 
        carbs_lines = "\nTotal Carbohydrates: " + str(self.nutritional_content["carbohydrates"]["total"]) + "\n\tDietary Fibers: " + str(self.nutritional_content["carbohydrates"]["fibers"]) + "\n\tTotal Sugars: " + str(self.nutritional_content["carbohydrates"]["sugars"]["total"]) + "\n\t\tAdded Sugars: " + str(self.nutritional_content["carbohydrates"]["sugars"]["added"])
        protein_lines = "\nProteins: " + str(self.nutritional_content["proteins"])
        return title_lines + fats_lines + other_lines + carbs_lines + protein_lines
    
    def __eq__(self, other):
        """ Returns whether two Ingredients are equal """
        key_list = self.get_key_list()
        for key in key_list:
            key_split = key.split()
            if self.get_at_key(key_split) != other.get_at_key(key_split):
                return False
        return self.name == other.get_name() and self.serving_size == other.get_serving_size()
    
    def get_name(self):
        """ Returns the name of the Ingredient. """
        return self.name
    
    def get_serving_size(self):
        """ Returns the serving size of the Ingredient. """
        return self.serving_size
    
    def get_nutritional_content(self):
        """ Returns the nutritional content of the Ingredient. """
        return self.nutritional_content

    def get_key_list(self, base_key = []):
        """ Returns a list of all the keys in the nutritional content dictionary. """
        key_list = []
        value = self.get_at_key(base_key)
        if type(value) == dict:
            lower_key_list = list(value.keys())
            for key in lower_key_list:
                new_key = base_key + [key]
                key_string = ""
                for key in new_key:
                    key_string += " " + key
                    key_string = key_string.strip()
                key_list.append(key_string)
                key_list = key_list + self.get_key_list(new_key)
        return key_list
            
    def get_at_key(self, key_list):
        """ Returns the nutritional value after traversing through the keys of key_list. """
        value = self.nutritional_content
        for key in key_list:
            value = value[key]
        return value