import psycopg2

# COMP 3005 A3 Part 1
# Bao Le 101223254

#Database Connection
db = psycopg2.connect(host = 'localhost', database = 'assignment3', user = 'postgres', password = 'comp3005')
    
if db is not None:
    print("Connected to database")


def getAllStudents():
    cursor = db.cursor() #creating cursor object so it can execute queries, get data, etc
    cursor.execute("SELECT * FROM students") #executing query to get all students
    students = cursor.fetchall() #fetchall() gets all rows in table and returns it as a list of tuples

    for student in students: #for each student, print student tuple
        print(student)

def addStudent(first_name, last_name, email, enrollment_date):
    cursor = db.cursor()
    #inserting  data into the specified columns with %s acting as placeholders for data
    query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
    values = (first_name, last_name, email, enrollment_date)
    cursor.execute(query, values) # putting together both query and values and executing them
    db.commit() # this line makes sure the data actually gets comitted to the table

def updateStudentEmail(student_id, new_email):
    cursor = db.cursor()
    #updating email to new email only if the studentid is equal to student_id
    query = f"UPDATE students SET email = '{new_email}' WHERE student_id = '{student_id}'"
    cursor.execute(query)
    db.commit()

def deleteStudent(student_id):
    cursor = db.cursor()
    cursor.execute(f"DELETE FROM students WHERE student_id = '{student_id}'")
    db.commit()



def main():
    getAllStudents()
    print("")
    #addStudent("Satoru", "Gojo", "satorugojo@gmail.com", "2024-01-01")
    print("")
    #updateStudentEmail(4, "poo@gmail.com")
    print("")
    #deleteStudent(5)
    return 0


if __name__ == "__main__":
    main()


    