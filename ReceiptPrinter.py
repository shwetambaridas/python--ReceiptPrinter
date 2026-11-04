item1 = input("Enter first item:")
item2 = input("Enter second item:")
item3 = input("Enter third item:")

price1 = float(input("Enter price of first item:"))
price2 = float(input("Enter price of second item:"))
price3 = float(input("Enter price of third item:"))

# Calculate total price
total_price = price1 + price2 + price3
tax = total_price * 0.18
grand_total = total_price + tax

# print receipt
print("\n" + "=" * 32)
print("         RECEIPT" + "" * 10)
print("\n" + "=" * 32)

print("Item".ljust(20) + "Price".rjust(10))
print("-" * 32)
print(f"{item1}".ljust(20) + f"{price1:.2f}".rjust(10))
print(f"{item2}".ljust(20) + f"{price2:.2f}".rjust(10))
print(f"{item3}".ljust(20) + f"{price3:.2f}".rjust(10))

print("-" * 32)
print("Subtotal".ljust(20) + f"{round(total_price, 2):>10.2f}")
print("Tax (18%)".ljust(20) + f"{round(tax, 2):>10.2f}")
print("=" * 32)
print("Grand Total".ljust(20) + f"{round(grand_total, 2):>10.2f}")
print("=" * 32)

print("\nThank you for shopping!")