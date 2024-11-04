# Input five numbers
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Prepare the data for output
squares = [num**2 for num in numbers]  # List of squares
cubes = [num**3 for num in numbers]    # List of cubes

# Display the output in a single print statement
print("Number:", *numbers)
print("Square:", *squares)
print("Cube:  ", *cubes)
