'''
Accept age, gender ('M', 'F'), and income and calculate the tax:
 Age >= 18 and < 60:
o Male:
 Income > 10,00,000: Tax = 30%
 Income between 5,00,000 and 10,00,000: Tax = 20%
 Income <= 5,00,000: Tax = 10%
o Female:
 Income > 10,00,000: Tax = 25%
 Income between 5,00,000 and 10,00,000: Tax = 15%
 Income <= 5,00,000: Tax = 5%
 Age >= 60:
o Male or Female:
 Income > 10,00,000: Tax = 20%
 Income <= 10,00,000: Tax = 10%
'''

age_data = int(input("Enter your age: "))
gender_data = input("Enter your gender (M/F): ").upper()
income_data = float(input("Enter your income: "))
if age_data >= 18 and age_data < 60:
    if gender_data == 'M':
        if income_data > 1000000:
            tax = income_data * 0.30
        elif 500000 < income_data <= 1000000:
            tax = income_data * 0.20
        else:
            tax = income_data * 0.10
    elif gender_data == 'F':
        if income_data > 1000000:
            tax = income_data * 0.25
        elif 500000 < income_data <= 1000000:
            tax = income_data * 0.15
        else:
            tax = income_data * 0.05
elif age_data >= 60:
    if income_data > 1000000:
        tax = income_data * 0.20
    else:
        tax = income_data* 0.10

print(f"Your calculated tax is: {tax:.2f}")