import tkinter as tk

def convert_to_uppercase():
    input_text = entry_text.get()
    uppercase_text = input_text.upper()
    result_label.config(text=f"Uppercase Text: {uppercase_text}")

# Create the main window
root = tk.Tk()
root.title("Uppercase Converter")

# Create and place entry widget for user input
entry_text = tk.Entry(root)
entry_text.grid(row=0, column=0, padx=10, pady=10)

# Create and place the button to convert to uppercase
convert_button = tk.Button(root, text="Convert to Uppercase", command=convert_to_uppercase)
convert_button.grid(row=1, column=0, pady=10)

# Create and place the label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, pady=10)

# Run the Tkinter main loop
root.mainloop()
