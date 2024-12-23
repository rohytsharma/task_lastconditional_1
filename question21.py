'''
Accept the price of an item from the user:
 If the price is greater than 1000, apply a 20% discount and print the new price.
 If between 500 and 1000, apply a 10% discount.
 If less than 500, no discount.
'''
price = float(input("Enter the price of the item: "))
if price > 1000:
    discount = price * 0.20
    new_price = price - discount
    print(f"Price is greater than 1000. A 20% discount is applied. New price: {new_price:.1f}")
elif 500 <= price <= 1000:
    discount = price * 0.10
    new_price = price - discount
    print(f"Price is between 500 and 1000. A 10% discount is applied. New price: {new_price:.1f}")
else:
    print(f"Price is less than 500. No discount applied. Price: {price:.1f}")