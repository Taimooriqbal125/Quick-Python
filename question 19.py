import math

# Input the radius of the sphere
radius = float(input("Enter the radius of the sphere: "))

# Calculate the volume of the sphere using the formula: V = (4/3) * π * r^3
volume = (4/3) * math.pi * (radius ** 3)

# Output the volume
print(f"The volume of the sphere is: {volume:.2f} cubic units")
