"""Start with "Welcome to the Haunted Castle".
 Ask the user to choose "enter the castle" or "run away".
 If "enter the castle", ask them to choose a door: "red", "green", or "black".
o If "red", print "You entered a room full of flames. Game Over."
o If "green", print "You found the treasure. You Win!"
o If "black", print "You were captured by ghosts. Game Over."
 If "run away", print "You escaped safely."""
print("Welcome to the Haunted Castle!")
action_data = input("Do you want to 'enter the castle' or 'run away'?: ").lower()

if action_data == "enter the castle":
    choice_door = input("Choose a door: 'red', 'green', or 'black': ").lower()
    if choice_door== "red":
        print("You entered a room full of flames.\nGame Over.")
    elif choice_door== "green":
        print("You found the treasure. You Win")
    elif choice_door == "black":
        print("You were captured by ghosts.\nGame Over.")
    else:
        print("Invalid door choice.\nGame Over.")
elif action_data == "run away":
    print("You escaped safely.")
else:
    print("Invalid choice.\nGame Over.")