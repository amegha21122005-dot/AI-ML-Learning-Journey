student_name=input("Enter student name:")
student_age=int(input("Enter student age:"))
student_marks=int(input("Enter student marks:"))
student_branch=input("Enter student branch:")

print("\n--- Student Details ---")
print("Name:", student_name)
print("Age:", student_age)
print("Branch:", student_branch)
print("Marks:", student_marks)

if(student_marks>=35):
    print("student have passed")
else:
    print("Fail")

if(student_marks>=90):
    print("Grade A")
elif(75<student_marks<89):
    print("Grade B")
elif(50<student_marks<74):
    print("Grade C")
else:
    print("Grade D")