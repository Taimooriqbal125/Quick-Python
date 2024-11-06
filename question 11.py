# Input the total number of classes held in the week
total_classes = 5

# Input the number of classes attended by the student
attendance = int(input("Enter the number of classes attended out of 5: "))

# Calculate the attendance percentage
attendance_percentage = (attendance / total_classes) * 100

# Output the result
print(f"The attendance percentage is: {attendance_percentage} % " )
