# Let's get the student's grade as a float input, just in case they got a decimal percent
grade = float(input("Enter your numerical grade (0-100): "))

# Start with Zero
gpa = 0.0

# Use if-elif-else, a lot..... 2 markers between each number to check the status
if grade >= 93:
    gpa = 4.0
elif grade >= 90:
    gpa = 3.7
elif grade >= 87:
    gpa = 3.3
elif grade >= 83:
    gpa = 3.0
elif grade >= 80:
    gpa = 2.7
elif grade >= 77:
    gpa = 2.3
elif grade >= 73:
    gpa = 2.0
elif grade >= 70:
    gpa = 1.7
elif grade >= 67:
    gpa = 1.3
elif grade >= 63:
    gpa = 1.0
elif grade >= 60:
    gpa = 0.7
else:
    gpa = 0.0

# Print out the student's grade
print(f"With a grade of {grade}, your GPA would be {gpa}")
