# Defines a class for a recipe with attributes and methods to manage it
class Recipe:

# Constructor to initialize the recipe with name, ingredients, steps, cooking time, and difficulty
    def __init__(self, name, ingredients, steps, cooking_time, difficulty):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.cooking_time = cooking_time
        self.difficulty = difficulty

# Methods to describe the recipe, add/remove ingredients, update cooking time, and add/remove steps
    def describe_recipe(self):
        print(f"Recipe: {self.name}")
        print(f"Cooking Time: {self.cooking_time} minutes")
        print(f"Difficulty: {self.difficulty}")
        print("Ingredients:", ', '.join(self.ingredients))
        print("Steps:")
        for i, step in enumerate(self.steps, 1):
           print(f"{i} . {step}")

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        print(f"{ingredient} has been added to the recipe.")

    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
            print(f"{ingredient} has been removed from the recipe.")
        else:
            print(f"{ingredient} is not in the recipe.")
    def update_cooking_time(self, new_time):
        self.cooking_time = new_time
        print(f"Cooking time has been updated to {self.cooking_time} minutes.")
    def add_step(self, step):
        self.steps.append(step)
        print(f"New step added: {step}")
    def remove_step(self, step):
        if step in self.steps:
            self.steps.remove(step)
            print(f"Step removed: {step}")
        else:
            print(f"Step not found: {step}")

# Inheritance example: QuickRecipe class that inherits from Recipe
class QuickRecipe(Recipe):
    def __init__(self, name, ingredients, steps, cooking_time, difficulty):

# Call the parent constructor to initialize the base attributes
        super().__init__(name, ingredients, steps, cooking_time, difficulty)
        if self.cooking_time > 15:
            print("⚠️ Warning: This recipe takes more than 15 minutes.")

    def is_really_quick(self):
        return self.cooking_time <= 15


# --- Simple User Usage 
def main():
    print("🍽️ Welcome to the Recipe Creator!")
    
    name = input("Enter the name of your recipe: ")
    cooking_time = int(input("Enter cooking time (in minutes): "))
    difficulty = input("Enter difficulty level (Easy, Medium, Hard): ")

    ingredients = input("Enter ingredients (separated by commas): ").split(",")
    ingredients = [item.strip() for item in ingredients]

    steps = input("Enter steps (separated by commas): ").split(",")
    steps = [item.strip() for item in steps]

    if cooking_time <= 15:
        recipe = QuickRecipe(name, ingredients, steps, cooking_time, difficulty)
    else:
        recipe = Recipe(name, ingredients, steps, cooking_time, difficulty)

    print("\n✅ Here's your recipe:")
    recipe.describe_recipe()

    # Let user add or remove an ingredient
    action = input("\nDo you want to add or remove an ingredient? (add/remove/skip): ").lower()
    if action == "add":
        new_ingredient = input("Enter the ingredient to add: ")
        recipe.add_ingredient(new_ingredient)
    elif action == "remove":
        ingredient_to_remove = input("Enter the ingredient to remove: ")
        recipe.remove_ingredient(ingredient_to_remove)

    # Option to update cooking time
    update_time = input("\nDo you want to update cooking time? (yes/no): ").lower()
    if update_time == "yes":
        new_time = int(input("Enter new cooking time: "))
        recipe.update_cooking_time(new_time)

    # Show final recipe
    print("\n📋 Final recipe:")
    recipe.describe_recipe()

    # QuickRecipe extra check
    if isinstance(recipe, QuickRecipe):
        print("\n⚡ Is it really quick?", recipe.is_really_quick())

if __name__ == "__main__":
    main()


