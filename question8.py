'''
Write a program starting with "Welcome to the Jungle Survival Challenge".
 Ask the user to "search for food" or "build a shelter".
 If "search for food", ask to choose between "hunt" or "gather".
 If "hunt", print "You were attacked by a wild animal. Game Over."
 If "gather", print "You found enough food. You Win!"
 If "build a shelter", print "Your shelter collapsed in the rain. Game Over."
'''
print("Welcome to the Jungle Survival Challenge!")
action_data = input("Do you want to 'search for food' or 'build a shelter'?: ").lower()

if action_data == "search for food":
    food_choice = input("Do you want to 'hunt' or 'gather'?: ").lower()
    if food_choice == "hunt":
        print("You were attacked by a wild animal.\nGame Over.")
    elif food_choice == "gather":
        print("You found enough food. You Win")
    else:
        print("Invalid choice.\nGame Over.")
elif action_data == "build a shelter":
    print("Your shelter collapsed in the rain.\nGame Over.")
else:
    print("Invalid choice. Game Over.")