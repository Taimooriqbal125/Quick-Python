# Input temperature in Fahrenheit from the user
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# Convert Fahrenheit to Centigrade (Celsius)
celsius = (fahrenheit - 32) * 5 / 9

# Convert Centigrade to Kelvin
kelvin = celsius + 273.15

# Output the results
print(f"The temperature in Centigrade is: {celsius:.2f} °C")
print(f"The temperature in Kelvin is: {kelvin:.2f} K")
