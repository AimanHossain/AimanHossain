import tkinter as tk
from tkinter import ttk

class ArithmeticOperations:
    def __init__(self, master):
        self.master = master
        self.master.title("Arithmetic Operations")

        self.result = tk.StringVar()

        # Entry widgets for input values
        self.entry_num1 = tk.Entry(self.master, width=10)
        self.entry_num1.grid(row=0, column=0, padx=10, pady=10)

        self.combo_operation = ttk.Combobox(self.master, values=['+', '-', '*', '/'])
        self.combo_operation.grid(row=0, column=1, padx=10, pady=10)

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
            operation = self.combo_operation.get()

            if operation == '+':
                self.result.set(num1 + num2)
            elif operation == '-':
                self.result.set(num1 - num2)
            elif operation == '*':
                self.result.set(num1 * num2)
            elif operation == '/':
                if num2 != 0:
                    self.result.set(num1 / num2)
                else:
                    self.result.set("Error: Division by zero")

            self.label_result.config(text=f"Result: {self.result.get()}")

        except ValueError:
            self.label_result.config(text="Error: Invalid input")


if __name__ == "__main__":
    root = tk.Tk()
    app = ArithmeticOperations(root)
    root.mainloop()
