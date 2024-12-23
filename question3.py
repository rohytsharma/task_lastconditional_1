"""
Take an employee's monthly salary as input. If it's more than 50,000, classify as
"High Earner". If less than or equal to 50,000, check if it's more than 20,000 to
classify as "Mid Earner", else classify as "Low Earner".
"""
salary_data = float(input("Enter the employee's monthly salary: "))
if salary_data > 50000:
    classification = "High Earner"
elif salary_data > 20000:
    classification = "Mid Earner"
else:
    classification = "Low Earner"

print(f"The employee is classified as a '{classification}'.")