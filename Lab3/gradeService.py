import helper
grade_file = open("grade.txt", "a+")
student_file = open("student.txt", "a+")

def add_grade():
    student_id = input("Please Enter student id: ")
    if helper.check_id(student_id,student_file):
        subject = input("Please Enter subject: ")
        grade = input("Please Enter grade: ")
        if not helper.check_grade(grade):
            raise Exception("invalid grade")
        grade_file.write(student_id+","+subject+","+grade + "\n")
        grade_file.flush()
    else:
        raise Exception("invalid id")

def print_subject_grades():    
    subject = input("Please Enter subject: ")
    grade_file.seek(0)
    for line in grade_file.readlines():
        if line.split(",")[1] == subject:
            print(line)


def get_average_grade():
    student_file.seek(0)
    student_list = []
    for line in student_file.readlines():
        formattedLine = line.strip().split(",")
        student_list.append({"id":formattedLine[0],"name":formattedLine[1],"sum":0,"subject_count":0})
    grade_file.seek(0)
    for line in grade_file.readlines():
        formattedLine = line.strip().split(",")
        index = int(formattedLine[0])-1
        student_list[index]["sum"]+=int(formattedLine[2])
        student_list[index]["subject_count"]+=1
    for student in student_list:
        if(student.get("subject_count")>0):
            print(f"{student.get("name")}   average:{student.get("sum")/student.get("subject_count")}")

def close_service():
    student_file.close()
    grade_file.close()