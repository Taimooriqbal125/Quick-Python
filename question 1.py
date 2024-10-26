age_years = int (input('enter your age in year'))

months = age_years * 12
days = age_years * 365  # Ignoring leap years
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("Your age in months:" ,months)
print("Your age in days:" ,days)
print("Your age in hours:" ,hours)
print("Your age in minutes:" ,minutes)
print("Your age in seconds:" ,seconds)