import tkinter as tk
from tkinter import filedialog, messagebox

class StringCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("String Counter App")

        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for the file name
        tk.Label(self.root, text="Select file:").grid(row=0, column=0, sticky="e")
        self.file_entry = tk.Entry(self.root)
        self.file_entry.grid(row=0, column=1)
        tk.Button(self.root, text="Browse", command=self.browse_file).grid(row=0, column=2)

        # Labels and Entry widgets for the strings to count
        strings_to_count = [
            "Hello my name is Peter Parker",
            "I love Python Programming",
            "Love",
            "Enemy"
        ]

        self.count_entries = []
        for i, string in enumerate(strings_to_count):
            tk.Label(self.root, text=f"Occurrences of '{string}':").grid(row=i + 1, column=0, sticky="e")
            entry = tk.Entry(self.root, state="readonly")
            entry.grid(row=i + 1, column=1, columnspan=2)
            self.count_entries.append(entry)

        # Button to perform the counting
        tk.Button(self.root, text="Count Occurrences", command=self.count_occurrences).grid(row=len(strings_to_count) + 1, column=0, columnspan=3, pady=10)

    def browse_file(self):
        file_name = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_name)

    def count_occurrences(self):
        file_name = self.file_entry.get()

        try:
            with open(file_name, "r") as file:
                content = file.read()

            # Count occurrences for each string
            strings_to_count = [
                "Hello my name is Peter Parker",
                "I love Python Programming",
                "Love",
                "Enemy"
            ]

            counts = {string: content.count(string) for string in strings_to_count}

            # Display the counts in the Entry widgets
            for entry, string in zip(self.count_entries, strings_to_count):
                entry.config(state="normal")
                entry.delete(0, tk.END)
                entry.insert(0, str(counts[string]))
                entry.config(state="readonly")

            messagebox.showinfo("Success", "Occurrences counted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error counting occurrences: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StringCounterApp(root)
    root.mainloop()
