'''
Write a program that starts with a greeting: "Welcome to the Forest Adventure".
 Prompt the user to choose a path: "left" or "right".
 If "left", ask them to pick between "explore" or "rest".
 If "explore", print "You found treasure!".
 If "rest", print "You were attacked by wild animals. Game Over."
 If "right", print "You fell into a trap. Game Over."
'''
print("Welcome to the Forest Adventure")
path_data = input("Choose a path: 'left' or 'right':\n ").lower()

if path_data == "left":
    choice = input("Do you want to 'explore' or 'rest'?: \n").lower()
    if choice == "explore":
        print("You found treasure")
    elif choice == "rest":
        print("You were attacked by wild animals.\nGame Over.")
    else:
        print("Invalid choice. Game Over.")
elif path_data == "right":
    print("You just fell into a trap.Sorry, Game Over.")
else:
    print("Invalid path.\nGame Over.")