def calculate_total(marks):
    total = sum(marks)
    return total
def calculate_percentage(total):
    percentage = total/5
    return percentage
def find_result(marks):
    for  mark in marks:
        if mark<35:
            return "Fail"
    return "Pass"
def find_highest_lowest(marks):
    highest = max(marks)
    lowest = min(marks)
    return highest,lowest
def find_grade(percentage):
    if percentage>=90:
        grade="A+"
    elif percentage>=80:
        grade= "A"
    elif percentage>=70:
        grade = "B"
    elif percentage>=60:
        grade = "C"
    elif percentage>=50:
        grade = "D"
    elif percentage<50:
        grade = "E"
    elif percentage<35:
        grade = "F"
    return grade