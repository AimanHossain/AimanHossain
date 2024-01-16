import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Enhanced Calculator App")

        self.result = tk.StringVar()

        # Entry widgets for input values
        self.entry_num1 = tk.Entry(self.master, width=10)
        self.entry_num1.grid(row=0, column=0, padx=10, pady=10)

        self.combo_operation_type = ttk.Combobox(self.master, values=['Arithmetic', 'Relational'])
        self.combo_operation_type.grid(row=0, column=1, padx=10, pady=10)
        self.combo_operation_type.set('Arithmetic')  # Default operation type

        self.entry_num2 = tk.Entry(self.master, width=10)
        self.entry_num2.grid(row=0, column=2, padx=10, pady=10)

        # Button to calculate result
        self.btn_calculate = tk.Button(self.master, text="Calculate", command=self.calculate)
        self.btn_calculate.grid(row=1, column=0, columnspan=3, pady=10)

        # Label to display the result
        self.label_result = tk.Label(self.master, text="Result:")
        self.label_result.grid(row=2, column=0, columnspan=3, pady=10)

    def calculate(self):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            operation_type = self.combo_operation_type.get()

            if operation_type == 'Arithmetic':
                result = self.perform_arithmetic_operation(num1, num2)
            elif operation_type == 'Relational':
                result = self.perform_relational_operation(num1, num2)
            else:
                result = "Invalid operation type"

            self.result.set(result)
            self.label_result.config(text=f"Result: {self.result.get()}")

        except ValueError:
            self.label_result.config(text="Error: Invalid input")

    def perform_arithmetic_operation(self, num1, num2):
        return num1 + num2  # You can add more arithmetic operations as needed

    def perform_relational_operation(self, num1, num2):
        return num1 < num2  # You can add more relational operations as needed

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
