''''
Take a number as input. Check if it is divisible by 2. If yes, further check if it is
divisible by 5. Print appropriate messages for each condition.'''
number_data = int(input("Enter a number: "))

if number_data % 2 == 0:
    print(f"{number_data} is divisible by 2.")
    if number_data % 5 == 0:
        print(f"{number_data} is also divisible by 5.")
    else:
        print(f"{number_data} is not divisible by 5.")
else:
    print(f"{number_data} is not divisible by 2.")