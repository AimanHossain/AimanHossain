from tkinter import *

root = Tk()
root.geometry("410x400")

def getvals():
    print(f"The value of name is {name_entry.get()}")
    print(f"The value of phone is {phone_entry.get()}")
    print(f"The value of gender is {gender_entry.get()}")
    print(f"The value of emergency is {emergency_entry.get()}")
    print(f"The value of payment is {payment_entry.get()}")

# Main label for the form
main_label = Label(root, text="Membership Form", font=("Helvetica", 16))
main_label.grid(row=0, column=2, padx=10, pady=10)

# Labels for Name, Phone, Gender, Emergency, and Payment Mode
name_label = Label(root, text="Name")
phone_label = Label(root, text="Phone")
gender_label = Label(root, text="Gender")
emergency_label = Label(root, text="Emergency Contact")
payment_label = Label(root, text="Payment Mode")

name_label.grid(row=1, column=1, padx=10, pady=5, sticky="e")
phone_label.grid(row=2, column=1, padx=10, pady=5, sticky="e")
gender_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")
emergency_label.grid(row=4, column=1, padx=10, pady=5, sticky="e")
payment_label.grid(row=5, column=1, padx=10, pady=5, sticky="e")

# Entry fields for user input
name_entry = Entry(root)
phone_entry = Entry(root)
gender_entry = Entry(root)
emergency_entry = Entry(root)
payment_entry = Entry(root)

name_entry.grid(row=1, column=2, padx=10, pady=5)
phone_entry.grid(row=2, column=2, padx=10, pady=5)
gender_entry.grid(row=3, column=2, padx=10, pady=5)
emergency_entry.grid(row=4, column=2, padx=10, pady=5)
payment_entry.grid(row=5, column=2, padx=10, pady=5)

# Checkbox for prebooking seat
prebook_checkbox = Checkbutton(root, text="Want to prebook your seat?")
prebook_checkbox.grid(row=6, column=2, padx=10, pady=5, sticky="w")

# Submit button
submit_button = Button(root, text="Submit to Company",command=getvals)
submit_button.grid(row=7, column=2, padx=10, pady=10)

root.mainloop()