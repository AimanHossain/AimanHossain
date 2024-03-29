import tkinter as tk
import re

class RegexCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Regex Checker App")

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for user input
        tk.Label(self.root, text="Enter a string:").grid(row=0, column=0, sticky="e")
        self.input_entry = tk.Entry(self.root)
        self.input_entry.grid(row=0, column=1, columnspan=2)

        # Radio buttons for different regex options
        self.regex_option = tk.StringVar()
        tk.Radiobutton(self.root, text="Only letters, numbers, and underscores", variable=self.regex_option, value="^[a-zA-Z0-9_]+$").grid(row=1, column=0, columnspan=3, sticky="w")
        tk.Radiobutton(self.root, text="Start with a specific number", variable=self.regex_option, value="^42").grid(row=2, column=0, columnspan=3, sticky="w")
        tk.Radiobutton(self.root, text="Find substrings within a string", variable=self.regex_option, value="substring").grid(row=3, column=0, columnspan=3, sticky="w")
        tk.Radiobutton(self.root, text="Match a word at the beginning", variable=self.regex_option, value="^Hello").grid(row=4, column=0, columnspan=3, sticky="w")

        # Button to check the user input
        tk.Button(self.root, text="Check Input", command=self.check_input).grid(row=5, column=0, columnspan=3, pady=10)

        # Result label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=6, column=0, columnspan=3)

    def check_input(self):
        user_input = self.input_entry.get()
        regex_pattern = self.regex_option.get()

        if not regex_pattern:
            self.result_label.config(text="Please select a regex option.")
            return

        try:
            match = re.match(regex_pattern, user_input)

            if match:
                self.result_label.config(text="Match successful!")
            else:
                self.result_label.config(text="No match found.")
        except re.error as e:
            self.result_label.config(text=f"Error in regex pattern: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RegexCheckerApp(root)
    root.mainloop()
