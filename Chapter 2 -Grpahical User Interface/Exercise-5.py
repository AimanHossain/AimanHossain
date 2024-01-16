import tkinter as tk
from tkinter import messagebox

def perform_operation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == 'Addition':
            result = num1 + num2
        elif operation == 'Subtraction':
            result = num1 - num2
        elif operation == 'Multiplication':
            result = num1 * num2
        elif operation == 'Division':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
        elif operation == 'Modulo Division':
            if num2 != 0:
                result = num1 % num2
            else:
                messagebox.showerror("Error", "Cannot perform modulo division by zero!")
                return
        else:
            messagebox.showerror("Error", "Invalid operation selected!")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("Arithmetic Calculator")

# Create and place entry widgets
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=0, column=1, padx=10, pady=10)

# Create and place operation selection dropdown
operations = ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Modulo Division']
operation_var = tk.StringVar(root)
operation_var.set(operations[0])

operation_dropdown = tk.OptionMenu(root, operation_var, *operations)
operation_dropdown.grid(row=0, column=2, padx=10, pady=10)

# Create and place the button to perform the operation
calculate_button = tk.Button(root, text="Calculate", command=perform_operation)
calculate_button.grid(row=1, column=0, columnspan=3, pady=10)

# Create and place the label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=2, column=0, columnspan=3, pady=10)

# Run the Tkinter main loop
root.mainloop()
