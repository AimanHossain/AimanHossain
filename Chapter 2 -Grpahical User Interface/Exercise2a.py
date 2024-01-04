from tkinter import *
import tkinter as tk
root = Tk()
root.title("Resizeable Labels")
root.geometry("400x500")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH,expand=TRUE)

#Create four labels and pack them 
label_1 = tk.Label(frame,text="Label 1",bg="red")
label_2 = tk.Label(frame,text="Label 2",bg="green")
label_3 = tk.Label(frame,text="Label 3",bg="blue")
label_4 = tk.Label(frame,text="Label 4",bg="yellow")

label_1.pack(side=tk.LEFT,fill=tk.BOTH,expand=TRUE)
label_2.pack(side=tk.LEFT,fill=tk.BOTH,expand=TRUE)
label_3.pack(side=tk.LEFT,fill=tk.BOTH,expand=TRUE)
label_4.pack(side=tk.LEFT,fill=tk.BOTH,expand=TRUE)

root.mainloop()
