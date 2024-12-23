'''
. Accept the age, gender ('M', 'F'), and show type ('Matinee', 'Evening'):
 Age < 12:
o Male or Female:
 Matinee: Ticket = Rs500
 Evening: Ticket = Rs700
 Age >= 12 and < 60:
o Male:
 Matinee: Ticket = Rs800
 Evening: Ticket = Rs100
o Female:
 Matinee: Ticket = Rs700
 Evening: Ticket = Rs900
 Age >= 60:
o Male or Female: Ticket = Rs600
'''
age_data = int(input("Enter your age: "))
gender_data = input("Enter your gender (M/F): ").upper()
show_data = input("Enter the show type (Matinee/Evening): ").capitalize()
if age_data < 12:
    if show_data == 'Matinee':
        ticket_price = 500
    elif show_data == 'Evening':
        ticket_price = 700
    else:
        ticket_price = None
elif 12 <= age_data < 60:
    if gender_data == 'M':  # Male
        if show_data == 'Matinee':
            ticket_price = 800
        elif show_data == 'Evening':
            ticket_price = 1000
        else:
            ticket_price = None
    elif gender_data == 'F':  # Female
        if show_data == 'Matinee':
            ticket_price = 700
        elif show_data == 'Evening':
            ticket_price = 900
        else:
            ticket_price = None
    else:
        ticket_price = None
elif age_data >= 60:
    ticket_price = 600
else:
    ticket_price = None
if ticket_price is not None:
    print(f"The ticket price is: Rs{ticket_price}")
else:
    print("Invalid input. Please check the show type or gender.")