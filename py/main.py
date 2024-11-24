from ingredient import Ingredient

d1 = {"calories": 1, "fats": {"total": 1, "saturated": 1, "trans": 1}, "cholesterol": 1, "sodium": 1, "carbohydrates": {"total": 1, "fibers": 1, "sugars": {"total": 1, "added": 1}}, "proteins": 1}
d2 = {"calories": 1, "fats": {"total": 1, "saturated": 1, "trans": 1}, "cholesterol": 1, "sodium": 1, "carbohydrates": {"total": 1, "fibers": 2, "sugars": {"total": 1, "added": 1}}, "proteins": 1}
i1 = Ingredient("Green Beans", 12, d1)
i2 = Ingredient("Green Beans", 12, d1)
i3 = Ingredient("Green Beans", 12, d2)
print(i1 == i2)
print(i2 == i3)
print(i1)