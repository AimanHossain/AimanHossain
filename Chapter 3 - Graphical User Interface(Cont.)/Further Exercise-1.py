import tkinter as tk
from tkinter import messagebox

class VendingMachine(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Vending Machine")
        
        
        self.items = {
            "Kinza Cola": 2.00,
            "Oman Chips": 1.50,
            "Mudhish Chips": 1.75,
            "Melco Juice": 2.50
        }
        self.selected_items = {}

        self.create_widgets()

    def create_widgets(self):
        # Display items
        for item, price in self.items.items():
            label = tk.Label(self, text=f"{item} - ${price:.2f}")
            label.pack()

        # Selection
        self.selection_var = tk.StringVar()
        self.selection_label = tk.Label(self, text="Select an item:")
        self.selection_label.pack()

        for item in self.items.keys():
            rb = tk.Radiobutton(self, text=item, variable=self.selection_var, value=item)
            rb.pack()

        # Buy button
        buy_button = tk.Button(self, text="Buy", command=self.buy_item)
        buy_button.pack()

    def buy_item(self):
        selected_item = self.selection_var.get()

        if selected_item:
            if selected_item not in self.selected_items:
                self.selected_items[selected_item] = 1
            else:
                self.selected_items[selected_item] += 1

            total_price = sum(self.items[item] * self.selected_items[item] for item in self.selected_items)

            messagebox.showinfo("Purchase Successful", f"Item: {selected_item}\nQuantity: {self.selected_items[selected_item]}\nTotal Price: ${total_price:.2f}")
        else:
            messagebox.showwarning("No Item Selected", "Please select an item before buying.")

if __name__== "_main_":
    vending_machine = VendingMachine()
    vending_machine.mainloop()