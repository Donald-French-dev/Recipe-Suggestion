# Global Variables

# List of recipe names, each with a comment for cuisine and dietary type
recipe_names = [
    "Vegetable Spring Rolls",           # Asian, Vegetarian
    "Thai Chicken Satay(with peanut sauce)", # Asian, None
    "Beef Bulgogi",                     # Asian, Gluten Free
    "Grilled Portobello Burger",        # American, Vegetarian
    "BBQ Ribs",                         # American, None
    "Classic Cheeseburger",             # American, Gluten Free
    "Caprese Salad",                    # Italian, Vegetarian
    "Polenta with Marinara Sauce",      # Italian, Gluten Free
    "Garlic Butter Spaghetti"           # Italian, None
]

# List of ingredients for each recipe, in the same order as recipe_names
recipe_ingredients = [
    ["rice paper", "cabbage", "carrots", "bell pepper", "onion", "garlic", "soy sauce", "oil", "egg wash"], # Vegetarian
    ["chicken", "coconut milk", "thai red curry paste", "soy sauce", "brown sugar", "garlic", "ginger", "peanut butter", "lime juice"], # None
    ["beef", "soy sauce", "brown sugar", "sesame oil", "garlic", "ginger", "onion", "black pepper", "sesame seeds"], # Gluten Free
    ["portobello mushrooms", "balsamic vinegar", "olive oil", "soy sauce", "rosemary", "garlic", "black pepper", "burger buns", "tomato", "red onion", "spinach", "avocado", "swiss cheese"], # Vegetarian
    ["pork ribs", "brown sugar", "chili powder", "garlic powder", "onion powder", "paprika", "salt", "black pepper", "apple cider vinegar", "barbecue sauce"], # None
    ["ground beef", "salt", "black pepper", "garlic powder", "burger buns", "american cheese", "tomato", "lettuce", "onion", "pickles", "ketchup", "mustard"], # Gluten Free
    ["tomatoes", "fresh mozzarella", "fresh basil", "olive oil", "balsamic glaze", "salt", "black pepper"], # Vegetarian
    ["polenta", "olive oil", "garlic", "salt", "marinara sauce", "parmesan cheese", "basil"], # Gluten Free
    ["spaghetti", "butter", "garlic", "olive oil", "salt", "black pepper", "parmesan cheese", "parsley"] # None
]

# List of cuisines for each recipe, in the same order as recipe_names
recipe_cuisines = [
    "Asian", "Asian", "Asian",
    "American", "American", "American",
    "Italian", "Italian", "Italian"
]

# List of dietary types for each recipe, in the same order as recipe_names
recipe_dietary = [
    "Vegetarian", "None", "Gluten Free",
    "Vegetarian", "None", "Gluten Free",
    "Vegetarian", "Gluten Free", "None"
]

# Function to greet the user and get their name
def welcome():
    name = input("What is your name? ")
    print(f"Hello, {name}! Welcome to the Personalized Recipe Suggestion System.")
    return name

# Function to get user preferences for cuisine, dietary restriction, and available ingredients
def get_preferences():
    # Get cuisine preference from user
    while True:
        cuisine = input("Choose a cuisine (American, Italian, Asian): ").strip().title() # cleans input to match what we expect
        if cuisine in ["American", "Italian", "Asian"]:
            break
        print("Sorry, we only serve American, Italian, or Asian.")

    # Get dietary restriction from user
    while True:
        diet = input("Any dietary restrictions? (Vegetarian, Gluten Free, None): ").strip().title()
        if diet in ["Vegetarian", "Gluten Free", "None", ""]:
            break
        print("Please enter 'Vegetarian', 'Gluten Free', 'None', or leave blank.")

    # Get list of ingredients user has
    ingredients_input = input("List ingredients you have (comma-separated): ").strip().lower()
    if ingredients_input == "" or ingredients_input in ["none", "nothing"]:
        ingredients = []
    else:
        # Split input into a list, removing extra spaces
        ingredients = [item.strip() for item in ingredients_input.split(",") if item.strip()]

    return cuisine, diet, ingredients

# Function to find recipes that match the user's preferences
def find_recipes(cuisine, diet, ingredients):
    matches = []
    for i in range(len(recipe_names)):
        # Check if cuisine matches
        if recipe_cuisines[i] != cuisine:
            continue
        # Check if dietary restriction matches (skip if user chose "None" or left blank)
        if diet and diet != "None" and recipe_dietary[i] != diet:
            continue
        # Check if at least one ingredient matches, or if user didn't specify any ingredients
        if ingredients:
            found = False
            for ing in recipe_ingredients[i]:
                if ing.lower() in ingredients:
                    found = True
                    break
            if not found:
                continue
        matches.append(i)
    return matches

# Function to display matching recipes to the user
def show_recipes(matches):
    if not matches:
        print("\nSorry, no recipes matched your criteria. Try again!")
        return False
    print("\nHere are some recipes you might like:")
    for idx in matches:
        print(f"\n{recipe_names[idx]}")
        print(f" - Ingredients: {', '.join(recipe_ingredients[idx])}")
        print(f" - Cuisine: {recipe_cuisines[idx]}")
        print(f" - Dietary: {recipe_dietary[idx]}")
    return True

# Main program loop
def main():
    welcome()
    while True:
        cuisine, diet, ingredients = get_preferences()
        matches = find_recipes(cuisine, diet, ingredients)
        if show_recipes(matches):
            break
        retry = input("Would you like to try again? (yes/no): ").strip().lower()
        if retry != "yes":
            print("Thank you for using the Personalized Recipe Suggestion System!")
            break

# Run the program if this file is executed directly
if __name__ == "__main__":
    main()