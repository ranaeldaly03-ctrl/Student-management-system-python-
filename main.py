import tkinter as tk
from database import create_db, add_student, get_students, delete_student, find_student, clear_students
from tkinter import messagebox


create_db()

window = tk.Tk()
window.title("Student Management System")
window.geometry("500x500")
window.configure(bg="#d8e3d5")


#add student gui
def add_stu():
    #get data from inputs
    name = name_entry.get()
    age =age_entry.get()
    course = course_entry.get()

    add_student(name, age, course)

    #clear inputs
    name_entry.delete(0,tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

    show_stu()


#show students
def show_stu():
    listbox.delete(0, tk.END)

    students = get_students()

    for student in students:
        listbox.insert(tk.END, student)   



#delete student
def delete_stu():
    selected = listbox.curselection()

    if selected:
        student = listbox.get(selected)
        student_id = student[0]

        delete_student(student_id)

        show_stu()



#search for a student
def find_stu():
    id = search_entry.get()

    results = find_student(id)

    listbox.delete(0, tk.END)

    for student in results:
        listbox.insert(tk.END, student)


#clear database
def clear_stu():
    if messagebox.askyesno("Warning", "Delete all students?"):
        clear_students()
        listbox.delete(0, tk.END)
          


#GUI title
title = tk.Label(window, text="Student Management System🧑‍💻", font=("Lilita One", 16, "bold"), bg="#768c71", fg="#d8e3d5")
title.pack(pady=10)

#name input 
name_label = tk.Label(window, text="Name", bg="#d8e3d5")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()


#age input
age_label = tk.Label(window, text="Age", bg="#d8e3d5")
age_label.pack()

age_entry = tk.Entry(window)
age_entry.pack()


#course input
course_label = tk.Label(window, text="Course", bg="#d8e3d5")
course_label.pack()

course_entry = tk.Entry(window)
course_entry.pack()


#search input
search_label = tk.Label(window, text="Search by ID", bg="#d8e3d5")
search_label.pack()

search_entry = tk.Entry(window)
search_entry.pack()

#Buttons
add_btn = tk.Button(window, text="ADD student", command=add_stu, bg="#9d8271")
add_btn.pack(pady=5)

show_btn = tk.Button(window, text="Show Students", command=show_stu, bg="#9d8271")
show_btn.pack(pady=5)

delete_btn = tk.Button(window, text="Delete Student", command=delete_stu, bg="#9d8271")
delete_btn.pack(pady=5)


search_btn = tk.Button(window, text="search", command=find_stu, bg="#9d8271")
search_btn.pack(pady=5)


clear_btn = tk.Button(window, text="Clear", command=clear_stu, bg="#9d8271")
clear_btn.pack(pady=5)


#listbox to show students
listbox = tk.Listbox(window, width=40, height=15, font=("Comic Sans", 12), bg="#d8e3d5")
listbox.pack(pady=10)


#run
window.mainloop()