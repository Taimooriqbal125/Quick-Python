import math

# Input the area of the circle
area = float(input("Enter the area of the circle: "))

# Calculate the radius using the formula: area = π * r^2
radius = math.sqrt(area / math.pi)

# Calculate the diameter (diameter = 2 * radius)
diameter = 2 * radius

# Calculate the circumference (circumference = 2 * π * radius)
circumference = 2 * math.pi * radius

# Output the diameter and circumference
print(f"The diameter of the circle is: {diameter:.2f}")
print(f"The circumference of the circle is: {circumference:.2f}")
