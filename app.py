# Recipe Manager Project

# This program allows the user to manage recipes.
# Users can add recipes, view all recipes, find quick recipes,
# and see recipe statistics such as average cooking time.


# Step 1: Data Structure Setup

# This line Creates four parallel lists to store recipe information.
recipe_names = ["Spaghetti", "Tacos", "Stir Fry"]
# This line is a list of recipe names
cook_times = [25, 15, 20]
# This line is a list of cooking times in minutes
difficulty_levels = [2, 1, 3]
# zThis line is a list of difficulty levels (1 = Easy, 5 = Hard)
ingredient_counts = [6, 8, 10]


# This line is a list of ingredient counts for each recipe


# Step 2: Display Menu Function

def display_menu():
    """Displays the main menu and returns user's choice"""
    print("\n=== Recipe Manager ===")
    # This is the Title header
    print("1. Add recipe")
    # This is the Menu option 1
    print("2. View recipes")
    # This is the Menu option 2
    print("3. Recipe statistics")
    # This is the Menu option 3
    print("4. Find by time")
    # This is the Menu option 4
    print("5. Exit")
    # This is the Menu option 5

    choice = input("Enter your choice (1-5): ")
    # This line asks for user choice
    return choice
    # This line returns the user's menu selection


# Step 3: Display All Recipes

def display_all_recipes():
    """Shows all recipes with their cook time, difficulty, and ingredient count"""
    print("\n--- All Recipes ---")
    # This line is the section header

    for i in range(len(recipe_names)):
        print(
            f"{i + 1}. {recipe_names[i]} - {cook_times[i]} mins - Difficulty {difficulty_levels[i]} - {ingredient_counts[i]} ingredients")
    # This Loops through all recipes and print their details
    # Previously had many bugs with this loop due to syntax errors


# Step 4: Add New Recipe

def add_new_recipe():
    """Lets the user add a new recipe and validates their input"""
    print("\n--- Add a New Recipe ---")
    # This is a section header

    while True:
        name = input("Enter recipe name: ").strip()
        # This line asks the user for a recipe name and validates it is not blank
        # Removes extra spaces from input
        if name == "":
            # This checks if input is empty
            print("Recipe name cannot be empty. Please try again.")
            # This lLine will show error message
        else:
            break
            # If a valid name is entered, program will exit loop

    # This line will ask for cook time and ensure it is a positive integer
    while True:
        try:
            time = int(input("Enter cook time (minutes): "))
            # Converts input to integer
            if time <= 0:
                # Validates positive number
                print("Time must be positive. Try again.")
                continue
                # Will ask again if invalid
            break
            # This will Exit the loop if valid
        except ValueError:
            # Catches error if input is not a number
            print("Invalid input. Please enter a number.")

    # Will ask for difficulty level and ensure it is between 1 and 5
    while True:
        try:
            difficulty = int(input("Enter difficulty level (1-5): "))  # Convert input to integer
            if difficulty < 1 or difficulty > 5:
                # Checks range
                print("Difficulty must be between 1 and 5.")
                continue
                # Asks again if invalid
            break
            # Exit loops if valid
        except ValueError:
            # Catches non-numeric input
            print("Invalid input. Please enter a number.")

    # Asks for ingredient count and ensure it is positive
    while True:
        try:
            ingredients = int(input("Enter number of ingredients: "))  # Convert input to integer
            if ingredients <= 0:
                # Validates positive number
                print("Number of ingredients must be positive.")
                continue
                # Asks again if invalid
            break
            # Exit loops if valid
        except ValueError:
            # Catches non-numeric input
            print("Invalid input. Please enter a number.")

    # Adds the validated data to all parallel lists
    recipe_names.append(name)
    # Adds new recipe name
    cook_times.append(time)
    # Adds corresponding cook time
    difficulty_levels.append(difficulty)
    # Adds corresponding difficulty
    ingredient_counts.append(ingredients)
    # Adds corresponding ingredient count

    print(f"'{name}' added successfully!")
    # Confirmation message at the end of program


# Step 5: Calculate Average Cook Time

def calculate_average_cook_time():
    """Calculates and returns the average cook time for all recipes"""
    total_time = sum(cook_times)
    # Adds up all cooking times
    avg_time = total_time / len(cook_times)
    # Divides the total by number of recipes
    return avg_time
    # Returns the calculated average


# Step 6: Find Quick Recipes

def find_quick_recipes(max_time):
    """Finds and displays recipes that can be made under a given cook time"""
    print(f"\n--- Recipes Under {max_time} Minutes ---")
    # This is a section header
    found = False
    # Flags to track if any recipes are found
    # Loops through all recipes
    for i in range(len(recipe_names)):
        if cook_times[i] <= max_time:
            # Checks if cook time is less than or equal to max_time
            print(f"- {recipe_names[i]} ({cook_times[i]} mins)")
            # Displays qualifying recipe
            found = True
            # Marks that at least one recipe was found
    if not found:
        # If no recipes matched the criteria prints message
        print("No recipes found within that time limit.")
        # Displays message


# Step 7: Display Recipe Statistics

def display_recipe_statistics():
    """Displays average cook time and total number of recipes"""
    print("\n--- Recipe Statistics ---")
    # Thia is a section header
    avg_time = calculate_average_cook_time()
    # Calls function to get average cook time
    print(f"Average cook time: {avg_time:.1f} minutes")
    # Shows average cooking time
    print(f"Total recipes: {len(recipe_names)}")
    # Shows total number of recipes


#  Step 8: Main Program Loop
def main():
    """Main loop that runs the Recipe Manager program"""
    while True:
        # Continues running until user chooses to exit
        choice = display_menu()
        # Shows menu and get user's choice

        # Matches user input to menu options
        if choice == "1":
            add_new_recipe()
            # Option 1: Adds recipe
        elif choice == "2":
            display_all_recipes()
            # Option 2: Views all recipes
        elif choice == "3":
            display_recipe_statistics()
            # Option 3: Shows statistics
        elif choice == "4":
            try:
                limit = int(input("Enter maximum cook time to search: "))  # Ask for time limit
                if limit <= 0:
                    # Validates that the input is positive
                    print("Please enter a positive number.")
                else:
                    find_quick_recipes(limit)
                    # Displays recipes under the limit
            except ValueError:
                # Handles invalid input
                print("Invalid input. Please enter a number.")
        elif choice == "5":
            print("Goodbye!")
            # Exits message
            break
            # Ends the loop to stop the program
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")  # Handle invalid menu choices


# Step 9: Run the Program

if __name__ == "__main__":
    # Checks if file is being run directly
    main()
    # Starts the main program loop again

