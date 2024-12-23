''''
Begin with "Welcome to the Cybersecurity Mission".
 Ask the user to "trace the hacker" or "secure the system".
 If "trace the hacker", ask to "track their IP" or "decode their message".
 If "track their IP", print "You caught the hacker. You Win!".
 If "decode their message", print "The message was a trap. Game
Over."
'''
print("Welcome, SOLDIER to the Cybersecurity Mission.")
trace_secure = input("Do you want to 'trace the hacker' or 'secure the system'?: ").lower()
if trace_secure == "trace the hacker":
    track_decode = input("Do you want to 'track their IP' or 'decode their message'?: ").lower()
    if track_decode == "track their ip":
        print("You caught the hacker. You Win.")
    elif track_decode == "decode their message":
        print("The message was a trap.You got hacked ha\nha\nha. \nGame Over.")
    else:
        print("Invalid choice.\nGame Over.")
elif trace_secure == "secure the system":
    shut_upgrade = input("Do you want to 'shut down the system' or 'upgrade the firewall'?: ")
    if shut_upgrade=="shut down the system":
        print("The attack was stopped. YOU WIN")
    elif shut_upgrade=="upgrade the firewall":
        print("The hacker bypassed it.\nGame Over.")
else:
    print("Invalid choice.\nGame Over.")