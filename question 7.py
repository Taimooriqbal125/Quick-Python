# Input the known values
car_average = 10.5  # Kilometers per liter
distance = 400  # Distance in kilometers
petrol_price = 150.23  # Petrol price per liter in rupees
tool_tax = 750  # Toll tax in rupees

# Calculate the total liters of petrol needed
liters_needed = distance / car_average

# Calculate the cost of petrol
petrol_cost = liters_needed * petrol_price

# Calculate the total money required (including toll tax)
total_money_required = petrol_cost + tool_tax

# Output the result
print("The total money required for the trip is: " , total_money_required)