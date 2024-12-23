'''
. Accept temperature in Celsius from the user:
 If greater than 40, print "Hot".
 If between 20 and 39, print "Warm".
 If less than 20, print "Cold".
'''
temperature_data = float(input("Enter the temperature in Celsius: "))
if temperature_data > 40:
    print("Hot")
elif 20 <= temperature_data <= 39:
    print("Warm")
else:
    print("Cold")