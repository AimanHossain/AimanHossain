import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
        unit = unit_var.get()

        if unit == 'Celsius':
            result = (temperature * 9/5) + 32
            result_unit = 'Fahrenheit'
        elif unit == 'Fahrenheit':
            result = (temperature - 32) * 5/9
            result_unit = 'Celsius'

        result_label.config(text=f"Result: {result:.2f} {result_unit}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid numeric value.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create and place entry widget for temperature
entry_temperature = tk.Entry(root)
entry_temperature.grid(row=0, column=0, padx=10, pady=10)

# Create and place unit selection radio buttons
unit_var = tk.StringVar()
unit_var.set('Celsius')

celsius_radio = tk.Radiobutton(root, text="Celsius", variable=unit_var, value='Celsius')
celsius_radio.grid(row=0, column=1, padx=10, pady=10)

fahrenheit_radio = tk.Radiobutton(root, text="Fahrenheit", variable=unit_var, value='Fahrenheit')
fahrenheit_radio.grid(row=0, column=2, padx=10, pady=10)

# Create and place the button to convert temperature
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=1, column=0, columnspan=3, pady=10)

# Create and place the label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=2, column=0, columnspan=3, pady=10)

# Run the Tkinter main loop
root.mainloop()
