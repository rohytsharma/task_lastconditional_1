''''
Write a program that starts with "Welcome to the Pirate Ship Adventure".
 Ask the user to choose between "searches for treasure" or "battle enemy
ships".
 If "search for treasure", ask whether to "dig on the island" or "explore the
cave".
 If "dig on the island", print "You found a hidden treasure chest. You
Win!"
 If "explore the cave", print "You were trapped inside. Game Over."
 If "battle enemy ships", ask if they want to "attack" or "defend".
 If "attack", print "You won the battle. You Win!"
 If "defend", print "You were outnumbered. Game Over."
'''
print("Welcome to the Pirate Ship Adventure!")
action_data = input("Do you want to 'search for treasure' or 'battle enemy ships'?: ").lower()

if action_data == "search for treasure":
    explore_dig = input("Do you want to 'dig on the island' or 'explore the cave'?: ").lower()
    if explore_dig == "dig on the island":
        print("You found a hidden treasure chest. YOU WIN. YOU ARE RICH ")
    elif explore_dig == "explore the cave":
        print("You were trapped inside.\nGame Over.")
    else:
        print("Invalid choice.\nGame Over.")
elif action_data == "battle enemy ships":
    attack_defend = input("Do you want to 'attack' or 'defend'?: ").lower()
    if attack_defend == "attack":
        print("You won the battle. YOU WIN")
    elif attack_defend == "defend":
        print("You were outnumbered.\nGame Over.")
    else:
        print("Invalid choice.\nGame Over.")
else:
    print("Invalid choice.\nGame Over.")