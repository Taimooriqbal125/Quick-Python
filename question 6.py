# Input purchase price, sale price, and number of copies sold
purchase_price = float(input("Enter the purchase price of the book: "))
sale_price = float(input("Enter the sale price of the book: "))
copies_sold = int(input("Enter the number of copies sold in a week: "))

# Calculate the profit per book
profit_per_book = sale_price - purchase_price

# Calculate the total profit
total_profit = profit_per_book * copies_sold

# Output the total profit
print("The total profit earned by the shopkeeper is:" , total_profit)
