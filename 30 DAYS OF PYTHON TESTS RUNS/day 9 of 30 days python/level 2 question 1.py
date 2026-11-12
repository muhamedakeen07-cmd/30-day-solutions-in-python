#level 2 question 1 of day 9/30 python

student_grades = int(input("Enter your Grades: "))


if student_grades >= 90 :
    print("Grade A excellent")

elif student_grades >= 80 :
    print("Grade B Good")

elif student_grades >= 70 :
    print("Grade C satisfied")
elif student_grades >= 60 :
    print("grade D decent")
elif student_grades >= 0 and student_grades <= 59:    
    print("Grade F failed")
else:
    print("Enter a valid marks")
