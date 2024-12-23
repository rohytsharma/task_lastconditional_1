'''Accept a number from the user:
 If the number is greater than 100, print "Big Number".
 If the number is between 50 and 100, print "Medium Number".
 If less than 50, print "Small Number".'''
number_input = int(input("Enter a number: "))
if number_input > 100:
    print("Big Number")
elif 50 <= number_input <= 100:
    print("Medium Number")
else:
    print("Small Number")