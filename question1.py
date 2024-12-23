"""
Take the price of an item as input. If the price is more than 1000, apply a 10%
discount. Otherwise, check if the price is more than 500 and apply a 5% discount.
Print the final price.
"""
price = float(input("Enter the price of the item: "))

if price > 1000:
    discount = price * 0.10
elif price > 500:
    discount = price * 0.05
else:
    discount = 0

final_price = price - discount
print(f"The final price after discount is: Rs.{final_price:.1f}")