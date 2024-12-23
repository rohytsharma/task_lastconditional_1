''''
Accept a BMI value from the user:
 If BMI < 18.5, print "Underweight".
 If 18.5 ≤ BMI < 24.9, print "Normal weight".
 If 25 ≤ BMI < 29.9, print "Overweight".
 If BMI ≥ 30, print "Obesity
'''
bmi_data = float(input("Enter your BMI value: "))
if bmi_data < 18.5:
    print("Underweight")
elif 18.5 <= bmi_data < 24.9:
    print("Normal weight")
elif 25 <= bmi_data < 29.9:
    print("Overweight")
else:  # bmi >= 30
    print("Obesity")