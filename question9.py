''''
Create a game with the message: "Welcome to the Space Adventure".
 Ask the user to choose "land on Mars" or "fly to Jupiter".
 If "land on Mars", ask if they want to "explore" or "build a base".
o If "explore", print "You found alien artifacts. You Win!"
o If "build a base", print "You ran out of resources. Game Over."
 If "fly to Jupiter", print "Your spaceship crashed. Game Over."
'''
print("Welcome to the Space Adventure!")

# Ask the user to choose between landing on Mars or flying to Jupiter
journey_data = input("Do you want to 'land on Mars' or 'fly to Jupiter'?: ").lower()

if journey_data == "land on mars":
    # Ask the user to choose between exploring or building a base
    action = input("Do you want to 'explore' or 'build a base'?: ").lower()
    if action == "explore":
        print("You found alien artifacts. You Win!")
    elif action == "build a base":
        print("You ran out of resources.\nGame Over.")
    else:
        print("Invalid choice.\nGame Over.")
elif journey_data== "fly to jupiter":
    print("Your spaceship crashed.\nGame Over.")
else:
    print("Invalid choice.\nGame Over.")