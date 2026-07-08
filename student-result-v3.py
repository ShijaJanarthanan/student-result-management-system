def get_student_details():
    student_name=input("Enter student name:")
    reg_no = int(input("Enter student register number:"))
    return student_name,reg_no
def get_marks():
    english_marks = int(input("Enter English Marks:"))
    science_marks = int(input("Enter Science Marks:"))
    social_marks = int(input("Enter Social Science  Marks:"))
    maths_marks = int(input("Enter Maths Marks:"))
    langII_marks = int(input("Enter LangII marks:"))
    marks=[english_marks,science_marks,
           social_marks,maths_marks,
           langII_marks]
    return marks
def calculate_total(marks):
    total = sum(marks)
    return total
def calculate_percent(total):
    percentage = total/5
    return percentage
def find_grade(percentage):
    if percentage>=90:
        grade = "A+"
    elif percentage>=80:
        grade = "A"
    elif percentage>=70:
        grade = "B"
    elif percentage>=60:
        grade = "C"
    elif percentage>=50:
        grade = "D"
    elif percentage>=35:
        grade = "E"
    else:
        grade = "F"
    return grade
def display_result(student_name, reg_no, total, percentage,result, grade):
    print("\n----------- STUDENT RESULT -----------")
    print("Student Name      :", student_name)
    print("Register Number   :", reg_no)
    print("Total Marks       :", total)
    print("Percentage        :", round(percentage, 2))
    print("Result            :", result)
    print("Grade             :", grade)
def main():
    student_name, reg_no = get_student_details()
    marks = get_marks()
    total = calculate_total(marks)
    percentage = calculate_percent(total)
    if percentage >= 35:
        result = "PASS"
    else:
        result = "FAIL"
    grade = find_grade(percentage)
    highest_marks = max(marks)
    lowest_marks = min(marks)
    print("Highest marks:",highest_marks)
    print("Lowest marks:",lowest_marks)
    display_result(student_name, reg_no, total, percentage,result,grade)
main()   
    


