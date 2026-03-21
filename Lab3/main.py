import gradeService
import studentService 

isRunning = True

while isRunning:
    choice = input('''
        Welcome to the student system!

        please choose an option:
        1) add a student
        2) add a grade
        3) print all students
        4) print student by id
        5) print grades of subject
        6) get average grade
        7) quit
    ''')
    try:
        if choice == '1':
            studentService.add_student()
        elif choice == '2':
            gradeService.add_grade()
        elif choice == '3':
            studentService.print_all_students()
        elif choice == '4':
            studentService.print_student_by_id()
        elif choice == '5':
            gradeService.print_subject_grades()
        elif choice == '6':
            gradeService.get_average_grade()
        elif choice == '7':
            studentService.close_service()
            gradeService.close_service()
            isRunning = False
        else:
            raise Exception("invalid choice")
    except Exception as e:
        print(e)


