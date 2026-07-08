student_name = input("Enter student name")
reg_no = int(input("Enter student register number"))
maths_marks = int(input("Enter maths marks:"))
chemistry_marks = int(input("Enter chemistry marks:"))
physics_marks = int(input("Enter physics marks:"))
computer_marks = int(input("Enter computer marks:"))
english_marks = int(input("Enter english marks:"))
langII_marks = int(input("Enter langII marks:"))
marks = [maths_marks,
    chemistry_marks,
    physics_marks,
computer_marks,
english_marks,
langII_marks]
total = sum(marks)
percentage = total/6
print("Student Name :", student_name)
print("Student Register number:",reg_no)
print("Maths marks:",maths_marks)
print("Chemistry Marks:",chemistry_marks)
print("Physics marks:", physics_marks)
print("Computer marks:",computer_marks)
print("English Marks:",english_marks)
print("Language II marks:", langII_marks)
print("\nTotal marks:   ",total)
print("Percentage:    ",round(percentage,2))
if percentage >=35:
    print("Result:   Pass")
else:
    print("Result:   Fail")
if percentage >=90 and percentage <=100:
    print("Grade:A+")
elif percentage >=80 and percentage <=89:
    print("Grade:A")
elif percentage >=70 and percentage <=79:
    print("Grade:B")
elif percentage >=60 and percentage <= 69:
    print("Grade:C")
elif percentage >=50 and percentage <=59:
    print("Grade:D")
elif percentage>=35 and percentage <=49:
    print("Grade:E")
elif percentage <34:
    print("F")
