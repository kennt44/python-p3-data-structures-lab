spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    pass

def get_spiciest_foods(spicy_foods):
    pass

def print_spicy_foods(spicy_foods):
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass
# Data
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# 1. Get names of all spicy foods
def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

# 2. Get foods with heat level > 5
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

# 3. Print spicy foods
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

# 4. Get spicy food by cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return next((food for food in spicy_foods if food['cuisine'] == cuisine), None)

def print_spiciest_foods(spicy_foods):
    for food in get_spiciest_foods(spicy_foods):
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    return total_heat // len(spicy_foods)

def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods
