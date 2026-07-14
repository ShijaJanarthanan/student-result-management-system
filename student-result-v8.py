def menu():
    print("==========================================\n")
    print("    Student Result Management System   \n")
    print("==========================================")
    print("\n------1.Add Student-------")
    print("\n------2.View Student------")
    print("\n------3.Search  Student------")
    print("\n------4.Update Student--------")
    print("\n------5.Exit--------------")
    print("==========================================\n")
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
student = None
def main():
    students = []
    while True:
        menu()
        choice = int(input("Enter your choice(1-5):"))
        if choice==1:
            student_name = input("Enter student name:")
            reg_no = int(input("Enter Student register name:"))
            english_marks = int(input("Enter english marks:"))
            lang11_marks = int(input("Enter language 11  marks:"))
            science_marks = int(input("Enter science marks:"))
            maths_marks = int(input("Enter maths marks:"))
            social_marks = int(input("Enter social marks:"))
            print("Student added successfully!")
            marks=[english_marks,lang11_marks,science_marks,social_marks,maths_marks]
           
            
            student = {
                        "name": student_name,
                        "reg_no": reg_no,
                        "english": english_marks,
                        "language": lang11_marks,
                        "science": science_marks,
                        "social": social_marks,
                         "maths": maths_marks
                        }
            students.append(student)
            total = calculate_total(marks)
            percentage = calculate_percentage(total)
            result = find_result(marks)
            if result=="Pass":
                grade = find_grade(percentage)
            else:
                grade = "No grade"
            highest,lowest=find_highest_lowest(marks)
            student["total"] = total
            student["percentage"] = percentage
            student["result"] = result
            student["grade"]  =grade
            student["highest"] = highest
            student["lowest"] = lowest
                    
           
        elif choice==2:
            if len(students)==0:
                print("No student data available.")
            else:
                for student in students:
                    print("\n===============Student Details==================")
                    print("Student Name:    ",     student["name"])
                    print("Register Number: ",   student["reg_no"])
                    print("English Marks:   ",  student["english"])
                    print("Language Marks:  ",   student["language"])
                    print("Science Marks:   ",   student["science"])
                    print("Social Marks:    ",   student["social"])
                    print("Maths Marks:     ",  student["maths"])
                    print("Total:           ", student["total"])
                    print("Percentage:      ", student["percentage"])
                    print("Result:          ", student["result"])
                    print("Grade:           ", student["grade"])
                    print("Highest Marks:   ", student["highest"])
                    print("Lowest Marks:    ", student["lowest"])
        elif choice ==3:
            search_reg = int(input("Enter Register Number to Search: "))
            found = False
            for student in students:
                if student["reg_no"] == search_reg:
                    print("\n===============Student Details==================")
                    print("Student Name:    ", student["name"])
                    print("Register Number: ", student["reg_no"])
                    print("English Marks:   ", student["english"])
                    print("Language Marks:  ", student["language"])
                    print("Science Marks:   ", student["science"])
                    print("Social Marks:    ", student["social"])
                    print("Maths Marks:     ", student["maths"])
                    print("Total:           ", student["total"])
                    print("Percentage:      ", student["percentage"])
                    print("Result:          ", student["result"])
                    print("Grade:           ", student["grade"])
                    print("Highest Marks:   ", student["highest"])
                    print("Lowest Marks:    ", student["lowest"])
                   
                    found = True
                    break
            if not found:
                print("Student not found.")  
        elif choice==4:
            update_reg= int(input("Enter register number to update:"))  
            found =False
            for student in students:
                if student["reg_no"]==update_reg:
                    english_marks = int(input("Enter new English marks: "))
                    lang11_marks = int(input("Enter new Language marks: "))
                    science_marks = int(input("Enter new Science marks: "))
                    maths_marks = int(input("Enter new Maths marks: "))
                    social_marks = int(input("Enter new Social marks: ")) 
                student["english"] = english_marks
                student["language"] = lang11_marks
                student["science"] = science_marks
                student["maths"] = maths_marks
                student["social"] = social_marks   
                marks = [
                            english_marks,
                            lang11_marks,
                            science_marks,
                            maths_marks,
                            social_marks
                        ]
                total= calculate_total(marks)
                percentage= calculate_percentage(total)
                result=find_result(marks)
                grade=find_grade(percentage)
                highest,lowest =find_highest_lowest(marks)
                student["total"] =total
                student["percentage"] =percentage
                student["result"] =result
                student["grade"] =grade
                student["highest"] =highest
                student["lowest"] =lowest
                print("Student details updated successfully!")
        elif  choice==5:
            print("Exit")
            break
        
        
main()



