# Input the number of kilograms of apples sold
kgs_sold = float(input("Enter the number of kilograms of apples sold: "))

# Input the sale price
sale_price = float(input("Enter the total sale price (including profit): "))

# Calculate the selling price per kilogram
selling_price_per_kg = sale_price / kgs_sold

# Since the selling price includes a 10% profit, we can calculate the purchase price
# Let purchase price be P. Then, selling price = P + 10% of P = 1.1 * P
# So, P = selling_price_per_kg / 1.1
purchase_price_per_kg = selling_price_per_kg / 1.1

# Output the purchase price per kilogram
print(f"The purchase price of 1 KG of apples is: {purchase_price_per_kg:.2f} rupees")
