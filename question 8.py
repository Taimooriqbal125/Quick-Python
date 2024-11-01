# Input the total number of chapters in the book
total_chapters = int(input("Enter the total number of chapters in the book: "))

# Input the number of chapters a student can complete in one day
chapters_per_day = int(input("Enter how many chapters the student can complete in one day: "))

# Input the number of study hours in a day
hours_per_day = float(input("Enter the number of hours the student studies per day: "))

# Calculate the total days required to complete the book
days_required = total_chapters / chapters_per_day

# Calculate the total hours required
total_hours = days_required * hours_per_day

# Output the result
print("The student requires hours to complete the book." ,total_hours)
