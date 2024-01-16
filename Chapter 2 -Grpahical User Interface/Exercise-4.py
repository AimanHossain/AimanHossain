import tkinter as tk
from tkinter import messagebox

def submit_form():
    student_name = entry_student_name.get()
    mobile_number = entry_mobile_number.get()
    email_id = entry_email_id.get()
    home_address = entry_home_address.get()
    gender = var_gender.get()
    course_enrolled = var_course_enrolled.get()
    english_communication = var_english_communication.get()
    languages_known = entry_languages_known.get()

    if not student_name or not mobile_number or not email_id or not home_address or not gender or not course_enrolled or not english_communication or not languages_known:
        messagebox.showerror("Error", "All fields are required.")
        return

    print(f"Student Name: {student_name}")
    print(f"Mobile Number: {mobile_number}")
    print(f"Email ID: {email_id}")
    print(f"Home Address: {home_address}")
    print(f"Gender: {gender}")
    print(f"Course Enrolled: {course_enrolled}")
    print(f"English Communication Skills: {english_communication}")
    print(f"Languages Known: {languages_known}")

root = tk.Tk()
root.title("Student Management System - New Student Registration")

label_student_name = tk.Label(root, text="Student Name")
label_student_name.grid(row=0, column=0)
entry_student_name = tk.Entry(root)
entry_student_name.grid(row=0, column=1)

label_mobile_number = tk.Label(root, text="Mobile Number")
label_mobile_number.grid(row=1, column=0)
entry_mobile_number = tk.Entry(root)
entry_mobile_number.grid(row=1, column=1)

label_email_id = tk.Label(root, text="Email ID")
label_email_id.grid(row=2, column=0)
entry_email_id = tk.Entry(root)
entry_email_id.grid(row=2, column=1)

label_home_address = tk.Label(root, text="Home Address")
label_home_address.grid(row=3, column=0)
entry_home_address = tk.Entry(root)
entry_home_address.grid(row=3, column=1)

var_gender = tk.StringVar()
radio_button_male = tk.Radiobutton(root, text="Male", variable=var_gender, value="Male")
radio_button_male.grid(row=4, column=0)
radio_button_female = tk.Radiobutton(root, text="Female", variable=var_gender, value="Female")
radio_button_female.grid(row=4, column=1)

var_course_enrolled = tk.StringVar()
check_button_bsc_cc = tk.Checkbutton(root, text="BSC CC", variable=var_course_enrolled, onvalue="BSC CC", offvalue="")
check_button_bsc_cc.grid(row=5, column=0)
check_button_bsc_cy = tk.Checkbutton(root, text="BSC CY", variable=var_course_enrolled, onvalue="BSC CY", offvalue="")
check_button_bsc_cy.grid(row=5, column=1)
check_button_bsc_psy = tk.Checkbutton(root, text="BSC PSY", variable=var_course_enrolled, onvalue="BSC PSY", offvalue="")
check_button_bsc_psy.grid(row=6, column=0)
check_button_ba_bm = tk.Checkbutton(root, text="BA & BM", variable=var_course_enrolled, onvalue="BA & BM", offvalue="")
check_button_ba_bm.grid(row=6, column=1)

var_english_communication = tk.StringVar()
scale_english_communication = tk.Scale(root, variable=var_english_communication, from_=1, to=5, orient="horizontal")
scale_english_communication.grid(row=7, columnspan=2)

label_languages_known = tk.Label(root, text="Languages Known")
label_languages_known.grid(row=8, column=0)
entry_languages_known = tk.Entry(root)
entry_languages_known.grid(row=8, column=1)

button_submit = tk.Button(root, text="Submit", command=submit_form)
button_submit.grid(row=9, columnspan=2)

root.mainloop()
