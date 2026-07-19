import pickle
student = None
def save_students(students):
    file = open("student_file.dat", "wb+")
    pickle.dump(students, file)
    file.close()
def load_students():
    try:
        file = open("student_file.dat", "rb")
        students = pickle.load(file)
        file.close()
        return students
    except FileNotFoundError:
        return []