'''
Accept two numbers from the user:
 If both numbers are even, print their sum.
 If one is even and the other is odd, print their difference.
 Otherwise, print their product.
'''
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a % 2 == 0 and b % 2 == 0:
    print("Both numbers are even. Their sum is:", a + b)
elif (a% 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0):
    print("One number is even and the other is odd. Their difference is:", abs(a - b))
else:
    print("Both numbers are odd. Their product is:", a * b)