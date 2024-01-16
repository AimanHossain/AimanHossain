import tkinter as tk
from tkinter import messagebox

def count_letters():
    input_text = entry_word.get()
    
    if not input_text:
        messagebox.showerror("Error", "Please enter a word.")
        return

    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    total_letters = len(input_text)
    num_vowels = sum(1 for char in input_text if char in vowels)
    num_consonants = sum(1 for char in input_text if char in consonants)
    num_special_characters = total_letters - (num_vowels + num_consonants)
    
    result_label.config(text=f"Total number of letters: {total_letters}\n"
                              f"Number of vowels: {num_vowels}\n"
                              f"Number of consonants: {num_consonants}\n"
                              f"Number of special characters: {num_special_characters}")

# Create the main window
root = tk.Tk()
root.title("Letter Counter")

# Create and place entry widget for user input
entry_word = tk.Entry(root)
entry_word.grid(row=0, column=0, padx=10, pady=10)

# Create and place the button to count letters
count_button = tk.Button(root, text="Count Letters", command=count_letters)
count_button.grid(row=1, column=0, pady=10)

# Create and place the label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, pady=10)

# Run the Tkinter main loop
root.mainloop()
