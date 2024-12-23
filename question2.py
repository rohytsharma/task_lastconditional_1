'''Ask the user if they want vegetarian or non-vegetarian. Based on the choice, give
them options. If vegetarian, ask if they want "Salad" or "Pasta". If non-vegetarian, ask
if they want "Chicken" or "Fish".'''
food_data = input("Do you prefer Vegetarian or Non-Vegetarian? (Please, Enter 'V' for Vegetarian or 'N' for Non-Vegetarian): ").strip().upper()


if food_data == 'V':
    veg_choice = input("Do you want \n'Salad' \n 'Pasta'?: ").capitalize()
    if veg_choice in ['Salad', 'Pasta']:
        print(f"You have chosen Vegetarian {veg_choice}.")
    else:
        print("Invalid choice. Please enter 'Salad' or 'Pasta'.")
elif food_data == 'N':
    nonveg_choice = input("choose what you want \nChicken\nFish:\n ").capitalize()
    if nonveg_choice in ['Chicken', 'Fish']:
        print(f"You have chosen Non-Vegetarian {nonveg_choice}.")
    else:
        print("Invalid choice. Please enter 'Chicken' or 'Fish'.")
else:
    print("Invalid preference. Please enter 'V' or 'N'.")