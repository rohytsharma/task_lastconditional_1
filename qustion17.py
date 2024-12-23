''''
Accept a color from the user:
 If the color is "Red", print "Stop".
 If "Yellow", print "Slow Down".
 If "Green", print "Go".
 Otherwise, print "Invalid Signal".
'''
color = input("Enter a color: ").lower()
if color == "red":
    print("stop")
elif color == "yellow":
    print("Slow Down")
elif color == "green":
    print("Go")
else:
    print("Invalid Signal")