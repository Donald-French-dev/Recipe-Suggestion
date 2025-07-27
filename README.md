# Personalized Recipe Suggestion System

## Overview

The **Personalized Recipe Suggestion System** is a simple, interactive Python application that helps users discover recipes based on their cuisine preferences, dietary restrictions, and available ingredients. The program suggests recipes from a curated list, making it easy to find meal ideas that fit your needs.

## Features

- **Cuisine Selection:** Choose from American, Italian, or Asian cuisines.
- **Dietary Restrictions:** Filter recipes by Vegetarian, Gluten Free, or None.
- **Ingredient Matching:** Enter ingredients you have, and get recipes that use them.
- **User-Friendly Interaction:** Guided prompts help you find the best recipe matches.

## How It Works

1. The program greets you and asks for your name.
2. You select your preferred cuisine and dietary restriction.
3. You list the ingredients you have on hand.
4. The system suggests recipes that match your criteria.
5. If no recipes match, you can try again with different preferences.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Running the Program

1. Clone or download this repository.
2. Open a terminal and navigate to the project directory.
3. Run the following command:

   ```bash
   python Recipe_Selection.py
   ```

4. Follow the on-screen prompts to get your recipe suggestions.

## Example Usage

```
What is your name? Alice
Choose a cuisine (American, Italian, Asian): Italian
Any dietary restrictions? (Vegetarian, Gluten Free, None): Vegetarian
List ingredients you have (comma-separated): tomato, basil, mozzarella

Here are some recipes you might like:

Caprese Salad
 - Ingredients: tomatoes, fresh mozzarella, fresh basil, olive oil, balsamic glaze, salt, black pepper
 - Cuisine: Italian
 - Dietary: Vegetarian
```

## Customization

You can expand the recipe database by editing the `Recipe_Selection.py` file and adding new entries to the `recipe_names`, `recipe_ingredients`, `recipe_cuisines`, and `recipe_dietary` lists.

## License

This project is provided for educational purposes.

## Author

Created by Don French.  
Feel free to contribute