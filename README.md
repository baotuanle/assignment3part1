COMP 3005 A3 Part 1
Bao Le 101223254

DISCLAIMER: It sounds like I'm not talking properly because I had a lip surgery done and my lip is swollen so I can not talk as proper as usual.

Video Link: https://youtu.be/rOA1x0AXIHk

Instructions:
- install psycopg2 the terminal:
	-"pip install psycopg2"

Testing:

-press 1 to get all students, 2 to add student, 3 to update student email, 4 to delete student, q to quit program
-Run it in VsCode with the "Run Code" triangle button.
-Second option: Run the command "python comp3005baoleA3Part1.py" in the terminal.

getAllStudents(): gets all students in database by creating cursor object and than executing a SELECT query on it, and then fetching all the data from it and then printing each student row.

addStudent(): adds student to database by creating cursor object and than executing a INSERT query on it.

updateStudentEmail(): updates student email to a new one by by creating cursor object and than executing a UPDATE query on it.

deleteStudent(): deletes all of the student data based on student id number by creating cursor object and than executing a DELETE query on it.
