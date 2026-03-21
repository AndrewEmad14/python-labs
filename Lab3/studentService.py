
import helper
student_file = open("student.txt", "a+")

def add_student():
    student = input("Please Enter your name: ")
    student_file.seek(0)
    next_id = len(student_file.readlines()) + 1
    student_file.write(str(next_id) + "," + student + "\n")
    student_file.flush()

def print_all_students():
    student_file.seek(0)
    for line in student_file.readlines():
        print(line)

def print_student_by_id():
    student_id = input("Please Enter student id: ")
    if helper.check_id(student_id,student_file):
        student_file.seek(0)
        for line in student_file.readlines():
            if line.split(",")[0] == student_id:
                print(line)
    else:
        raise Exception("invalid id")
    
def close_service():
    student_file.close()
