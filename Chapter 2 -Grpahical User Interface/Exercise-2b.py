import tkinter as tk

root = tk.Tk()
root.geometry("300x400")
root.title("Resizable Labels")

# Create left frame with a border
frame_left = tk.Frame(root, bd=5,)
frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True,)

# Create right frame with a border
frame_right = tk.Frame(root, bd=5)
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Create labels A, B, C, and D with background colors
label_a = tk.Label(frame_left, text="Label A",fg="white", bg="black")
label_b = tk.Label(frame_left, text="Label B", bg="white")
label_c = tk.Label(frame_right, text="Label C", bg="white")
label_d = tk.Label(frame_right, text="Label D",fg="white", bg="black")

# Pack labels A and C at the top of their frames
label_a.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
label_c.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Pack labels B and D at the bottom of their frames
label_b.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
label_d.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

root.mainloop()
