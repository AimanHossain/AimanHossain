import tkinter as tk

# Create a function to change the label font style
def change_font(label):
    label.config(font=("Helvetica", 16, "bold"))

# Create the main window
root = tk.Tk()
root.title("Welcome Message")

# Set the default window size
root.geometry("400x200")

# Disable window resizing
root.resizable(False, False)

# Add a background color to the window
root.configure(bg="lightblue")

# Create a label to display the welcome message
welcome_label = tk.Label(root, text="Welcome to My App", font=("Arial", 14), bg="lightblue")
welcome_label.pack(pady=50)

# Create a button to change the label font style
font_button = tk.Button(root, text="Change Font", command=lambda: change_font(welcome_label))
font_button.pack()

# Start the GUI event loop
root.mainloop()
