import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Add your authentication logic here
    if username == "your_username" and password == "your_password":
        result_label.config(text="Login successful")
    else:
        result_label.config(text="Login failed")

root = tk.Tk()
root.geometry("300x400")
root.title("Login Page")

# Create and arrange widgets using the grid geometry manager

# Username Label and Entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password Label and Entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

password_entry = tk.Entry(root, show="*")  # Passwords should be hidden
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Login Button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="", fg="red")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
