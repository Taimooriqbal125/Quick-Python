# Input three numbers from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Interchanging the values without using a fourth variable
a, b, c = c, a, b

# Output the interchanged values
print("After interchanging:")
print(f"First number: {a}")
print(f"Second number: {b}")
print(f"Third number: {c}")
