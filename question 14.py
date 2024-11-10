# Input the coordinates of the two points
x1 = float(input("Enter the x-coordinate of point P: "))
y1 = float(input("Enter the y-coordinate of point P: "))
x2 = float(input("Enter the x-coordinate of point Q: "))
y2 = float(input("Enter the y-coordinate of point Q: "))

# Calculate the slope (m) of the line
if x2 - x1 != 0:  # To avoid division by zero
    slope = (y2 - y1) / (x2 - x1)
else:
    slope = None  # This means the line is vertical

# Display the equation of the line
if slope is not None:
    # Equation in the form y = mx + b
    # Calculate the y-intercept (b)
    intercept = y1 - slope * x1
    print(f"The equation of the line is: y = {slope:.2f}x + {intercept:.2f}")
else:
    print(f"The equation of the line is: x = {x1} (vertical line)")
