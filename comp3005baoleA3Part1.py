import psycopg2
from datetime import date

# COMP 3005 A3 Part 1
# Bao Le 101223254

#Database Connection
db = psycopg2.connect(host = 'localhost', database = 'assignment3', user = 'postgres', password = 'comp3005')
    
if db is not None:
    print("Connected to database")


def getAllStudents():
    try:
        cursor = db.cursor() #creating cursor object so it can execute queries, get data, etc
        cursor.execute("SELECT * FROM students") #executing query to get all students
        students = cursor.fetchall() #fetchall() gets all rows in table and returns it as a list of tuples

        print("student_id first_name last_name email enrollment_date")
        for student in students: #for each student, print student tuple
            enrollment_date = student[4].strftime("%Y-%m-%d") #this is so the date displays properly when i print out the student date
            print(f"{student[0]} {student[1]} {student[2]} {student[3]} {enrollment_date}")
    except Exception as e:
        print("An error occurred while fetching students:")

def addStudent(first_name, last_name, email, enrollment_date):
    try:
        cursor = db.cursor()
        #inserting  data into the specified columns with %s acting as placeholders for data
        query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
        values = (first_name, last_name, email, enrollment_date)
        cursor.execute(query, values) # putting together both query and values and executing them
        db.commit() # this line makes sure the data actually gets comitted to the table
        print("Student added")
    except Exception as e:
        print("An error occurred while adding student:", e)

def updateStudentEmail(student_id, new_email):
    try:
        cursor = db.cursor()
        #Error checking to make sure the student id exists in the database
        cursor.execute(f"SELECT * FROM students WHERE student_id = '{student_id}'")
        #fetching only first row since each student id is unique to a one student
        containsStudent = cursor.fetchone()

        if containsStudent:
            #updating email to new email only if the studentid is equal to student_id
            query = f"UPDATE students SET email = '{new_email}' WHERE student_id = '{student_id}'"
            cursor.execute(query)
            db.commit()
            print("Updated student")
        else:
            print("Student ID does not exist.")
    except Exception as e:
        print("An error occurred while updating student email:", e)

def deleteStudent(student_id):
    try:
        cursor = db.cursor()
        #Error checking to make sure the student id exists in the database
        cursor.execute(f"SELECT * FROM students WHERE student_id = '{student_id}'")
        #fetching only first row since each student id is unique to a one student
        containsStudent = cursor.fetchone()
        if containsStudent:
            cursor.execute(f"DELETE FROM students WHERE student_id = '{student_id}'")
            db.commit()
            print("Deleted student")
        else:
            print("Student ID does not exist.")
    except Exception as e:
        print("An error occurred while deleting student:", e)

def main():
    while True:
        print("\n")
        print("1. Get all students")
        print("2. Add student")
        print("3. Update a student's email")
        print("4. Delete student")
        print("Q. Exit")
        choice = input("Enter your choice: ")
        print("\n")

        if choice == "1":
            getAllStudents()
        elif choice == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == "3":
            student_id = input("Enter student ID: ")
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)
        elif choice == "4":
            student_id = input("Enter student ID to delete: ")
            deleteStudent(student_id)
        elif choice.lower() == "q":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4 or Q.")

    return 0


if __name__ == "__main__":
    main()


    
