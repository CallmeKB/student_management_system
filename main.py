from database import get_connection
from student import Student
from student_repo import add_student
from student_repo import view_student,search_student, update_student,check_student, delete_student
import time

connection = get_connection()



def display_menu():
    print("""
    ===== STUDENT MANAGEMENT SYSTEM =====

    1. Add Student
    2. View Students
    3. Search Student
    4. Update Student
    5. Delete Student

    0. Exit
    """)


while True:
    display_menu()
    choice = int(input("Enter your choice...."))

    match choice:
        case 1:
            name = input("Enter student's name:")
            age= int(input("Enter student's age:"))
            email = input("Enter student's email:")

            std = Student(name, age, email)
            add_student(std)
            

            print("Student added succesfully....")
            time.sleep(1)

        case 2:
            view_student()
            time.sleep(1)

        case 3:
            search_name = input("Enter the name of a student: ")
            search_student(search_name)

        case 4:

            student_id = int(input("Enter student id to update: "))
            check_student(student_id)

            student = check_student(student_id)

            if not student:
                print("Student ID not found.....")
                continue
            

            update_student(student_id)
            print("Succesfully Updated.....")

        case 5:

            student_id = int(input("Enter student id to delete: "))
            check_student(student_id)

            student = check_student(student_id)

            if not student:
                print("Student ID not found.....")
                continue

            delete_student(student_id)   
            
        case 0:
            print("Exiting Student Management System....")
            break
