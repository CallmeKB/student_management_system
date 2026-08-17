from database import get_connection
from student import Student
import time

def add_student(student):

    conn = get_connection()
    c = conn.cursor()

    query="""
    INSERT INTO students(name, age, email)
    VALUES(%s, %s, %s)
    """
    c.execute(query,(student.name, student.age, student.email))

    conn.commit()
    conn.close()


def view_student():

    conn = get_connection()
    c = conn.cursor()

    query="""
    SELECT * FROM students
    """
    c.execute(query)
    value = c.fetchall()
    for x in value:
        print(f"Student ID: {x[0]}")
        time.sleep(.5)
        print(f"Name: {x[1]}")
        time.sleep(.5)
        print(f"Age: {x[2]}")
        time.sleep(.5)
        print(f"Email: {x[3]}")
        time.sleep(.5)
        print("\n")

    conn.close()


def search_student(search_name):

    conn = get_connection()
    c = conn.cursor()

    query="""
    SELECT * FROM students
    WHERE name LIKE %s
    """

    search_name=f"%{search_name}%"
    c.execute(query, (search_name,))
    value = c.fetchall()

    if not value:
        print("No matching Student found.....")
        conn.close()
        return


    for x in value:
        print(f"Student ID: {x[0]}")
        time.sleep(.5)
        print(f"Name: {x[1]}")
        time.sleep(.5)
        print(f"Age: {x[2]}")
        time.sleep(.5)
        print(f"Email: {x[3]}")
        time.sleep(.5)
        print("\n")

    conn.close()


def update_student(student_id):

    conn = get_connection()
    c = conn.cursor()   

    print("""
    1. Update Name
    2. Update Age
    3. Update Email
    """)

    try:
        update_choice = int(input("Enter choice: "))
    except ValueError:
        print("enter valid choice")
        conn.close()
        return

    match update_choice:
        case 1:
            update = input("Enter updated name: ")
            query = """
            UPDATE students
            SET name = %s
            WHERE id = %s
            """

            c.execute(query,(update, student_id))
            conn.commit()

        case 2:
            update = input("Enter updated age: ")
            query = """
            UPDATE students
            SET age = %s
            WHERE id = %s
            """

            c.execute(query,(update, student_id))
            conn.commit()

        case 3:
            update = input("Enter updated email: ")
            query = """
            UPDATE students
            SET email = %s
            WHERE id = %s
            """

            c.execute(query,(update, student_id))
            conn.commit()

        case _:
            print("invalid choice.....")


    conn.close()


def check_student(student_id):

    conn = get_connection()
    c = conn.cursor()   

    query= """
    SELECT * FROM students
    WHERE id = %s
    """
    c.execute(query ,(student_id,))

    value = c.fetchone()

    conn.close()

    return value



def delete_student(student_id):

    conn = get_connection()
    c = conn.cursor()   

    query= """
    DELETE FROM students
    WHERE id = %s
    """
    c.execute(query ,(student_id,))

    conn.commit()
    conn.close()
    print('Student deleted succesfully......')
    