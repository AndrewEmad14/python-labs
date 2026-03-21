def check_id(student_id,student_file):
    if not student_id.isdigit() and (int(student_id) < 1 or int(student_id) > len(student_file.readlines())):
        return False
    student_file.seek(0)
    for line in student_file.readlines():
        print(line.split(",")[0])
        if line.split(",")[0] == student_id:
            return True
    return False

def check_grade(grade):
    if not grade.isdigit() and (int(grade) < 0 or int(grade) > 100):
        return False
    return True