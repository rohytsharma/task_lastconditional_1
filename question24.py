'''
Accept the age, gender ('M', 'F'), and experience (years) and assign a role:
 Age >= 21 and <= 35:
o Male:
 Experience >= 5: "Senior Developer"
 Experience < 5: "Junior Developer"
o Female:
 Experience >= 5: "Senior Analyst"
 Experience < 5: "Junior Analyst"
 Age > 35:
o Male or Female: "Manager Role"
'''
age_data = int(input("Enter your age: "))
gender_data = input("Enter your gender (M/F): ").upper()
experience_data = int(input("Enter your years of experience: "))

if 21 <= age_data <= 35:
    if gender_data == 'M':
        if experience_data >= 5:
            print("Senior Developer")
        else:
            print("Junior Developer")
    elif gender_data == 'F':
        if experience_data >= 5:
            print("Senior Analyst")
        else:
            print("Junior Analyst")
    else:
        print("Invalid gender input.")
elif age_data > 35:
    print("Manager Role")
else:
    print("Not eligible due to age restrictions.")