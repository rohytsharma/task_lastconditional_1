'''
Write a program to input three numbers and find the largest among them using nested
if-else.
'''
num_data_1 = float(input("Enter the first number: "))
num_data_2 = float(input("Enter the second number: "))
num_data_3 = float(input("Enter the third number: "))

if num_data_1 >= num_data_2:
    if num_data_1 >= num_data_3:
        largest = num_data_1
    else:
        largest = num_data_3
else:
    if num_data_2 >= num_data_3:
        largest = num_data_2
    else:
        largest = num_data_3

print(f"The largest number is: {largest}")