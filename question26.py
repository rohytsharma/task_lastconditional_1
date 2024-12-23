'''
Accept the age, gender ('M', 'F'), and membership type ('Monthly', 'Yearly'):
 Age >= 18 and < 30:
o Male:
 Monthly: Rs50
 Yearly: Rs500
o Female:
 Monthly: Rs45
 Yearly: Rs450
 Age >= 30 and <= 50:
o Male or Female:
 Monthly: Rs60
 Yearly: Rs600
 Age > 50:
o Male or Female:
 Monthly: Rs40
 Yearly: Rs400
'''
age_data = int(input("Enter your age: "))
gender_data = input("Enter your gender (M/F): ").upper()
membership_data = input("Enter the membership type (Monthly/Yearly): ").capitalize()
if 18 <= age_data < 30:
    if gender_data == 'M':
        if membership_data == 'Monthly':
            fee = 50
        elif membership_data == 'Yearly':
            fee = 500
        else:
            print("No fees for you")
            fee = None
    elif gender_data == 'F':
        if membership_data == 'Monthly':
            fee = 45
        elif membership_data == 'Yearly':
            fee = 450
        else:
            print("No fees for you")
            fee = None
    else:
        fee = None
elif 30 <= age_data <= 50:
    if membership_data == 'Monthly':
        fee = 60
    elif membership_data == 'Yearly':
        fee = 600
    else:
        print("No fees for you")
        fee =None
elif age > 50:
    if membership_data== 'Monthly':
        fee = 40
    elif membership_data== 'Yearly':
        fee = 400
    else:
        print("No fees for you")
        fee = None
else:
    fee = None
if fee is not None:
    print(f"The membership fee is: Rs{fee}")
else:
    print("Invalid input. Please check the membership type or other details.")