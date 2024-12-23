'''
Accept the age, gender ('M', 'F'), and academic score (out of 100) and determine
eligibility:
 Age >= 18 and <= 25:
o Male:
 Score >= 85: "Full Scholarship"
 Score >= 70: "Partial Scholarship"
 Score < 70: "No Scholarship"
o Female:
 Score >= 80: "Full Scholarship"
 Score >= 65: "Partial Scholarship"
 Score < 65: "No Scholarship"
'''
age_data = int(input("Enter your age: "))
gender_data = input("Enter your gender (M/F): ").upper()
score_data = float(input("Enter your academic score (out of 100): "))

if 18 <= age_data <= 25:
    if gender_data == 'M':
        if score_data >= 85:
            print("Full Scholarship")
        elif score_data >= 70:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
    elif gender_data == 'F':
        if score_data >= 80:
            print("Full Scholarship")
        elif score_data >= 65:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
    else:
        print("Invalid gender input.")
else:
    print("Not eligible due to age restrictions.")