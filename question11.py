'''
Begin with "Welcome to the Underwater World".
 Ask the user to choose "dive deeper" or "surface".
 If "dive deeper", ask them to "search for pearls" or "chase the fish".
o If "search for pearls", print "You found a rare pearl. You Win!"
o If "chase the fish", print "You got lost underwater. Game Over."
 If "surface", print "You returned safely."
'''


print("Welcome to the Underwater World!")
action_data = input("Do you want to 'dive deeper' or 'surface'?: ").lower()
if (action_data == "dive deeper"):
    search_data = input("Do you want to 'search for pearls' or 'chase the fish'?: ").lower()
    if search_data == "search for pearls":
        print("You found a rare pearl. You Win")
    elif search_data== "chase the fish":
        print("You got lost underwater.\nGame Over.")
    else:
        print("Invalid choice.\nGame Over.")
elif action_data == "surface":
    print("You returned safely.")
else:
    print("Invalid choice.\nGame Over.")