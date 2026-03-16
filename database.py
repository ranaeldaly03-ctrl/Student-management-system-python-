#crate database  --> students
#add student
#show all students
#delet student

import sqlite3

def create_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS students(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   age INTEGER,
                   course TEXT)""")
    
    conn.commit()
    conn.close


def add_student(name, age, course):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO students(name, age, course) VALUES(?, ?, ?)", (name, age, course))   

    conn.commit()
    conn.close()



def get_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()
    return rows


def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))

    conn.commit()
    conn.close()



def find_student(id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE id= ?", (id,))
    rows = cursor.fetchall()

    conn.close()
    return rows   


def clear_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students")

    conn.commit()
    conn.close()