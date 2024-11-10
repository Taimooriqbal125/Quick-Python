import math 
# Input the hypotenuse and base of the triangle
hypotenuse = float(input("Enter the length of the hypotenuse: "))
base = float(input("Enter the length of the base: "))

# Calculate the altitude using the Pythagorean theorem
# altitude^2 + base^2 = hypotenuse^2
# So, altitude = sqrt(hypotenuse^2 - base^2)
altitude = math.sqrt (hypotenuse**2 - base**2)

# Output the altitude
print(f"The altitude of the triangle is: {altitude:.2f}")
