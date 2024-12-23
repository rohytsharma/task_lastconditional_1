'''
Start the program with "Welcome to the Wizarding World".
 Ask the user to choose a subject: "spells" or "potions".
 If "spells", ask them to "practice magic" or "compete in duels".
 If "practice magic", print "You mastered a powerful spell. You Win!"
 If "compete in duels", print "You lost to a rival wizard. Game Over."
 If "potions", ask whether to "brew an elixir" or "create poison".
 If "brew an elixir", print "You healed a village. You Win!"
 If "create poison", print "Your potion backfired. Game Over."
'''
print("Welcome to the Wizarding World!")
spell_potions = input("Do you want to study 'spells' or 'potions'?: ").lower()

if spell_potions == "spells":
    magic_duels = input("Do you want to 'practice magic' or 'compete in duels'?: ").lower()
    if magic_duels == "practice magic":
        print("You mastered a powerful spell. \nYOU WIN! WITCH")
    elif magic_duels == "compete in duels":
        print("You lost to a rival wizard.\nGame Over.")
    else:
        print("Invalid choice.\nGame Over.")
elif spell_potions == "potions":
    elixir_poison = input("Do you want to 'brew an elixir' or 'create poison'?: ").lower()
    if elixir_poison == "brew an elixir":
        print("You healed a village. YOU WIN ")
    elif elixir_poison == "create poison":
        print("Your potion backfired.\nGame Over. WITCH.")
    else:
        print("Invalid choice.\nGame Over.")
else:
    print("Invalid choice.\nGame Over.")