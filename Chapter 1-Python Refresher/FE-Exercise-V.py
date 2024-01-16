marks = [
    ("CodeLab I", 67),
    ("Web Development", 75),
    ("CodeLab II", 74),
    ("Smartphone Apps", 68),
    ("Games Development", 70),
    ("Responsive Web", 65)
]

# Sort by marks from low to high
sorted_low_to_high = sorted(marks, key=lambda x: x[1])
print("Sorted by Marks (Low to High):", sorted_low_to_high)

# Sort by marks from high to low
sorted_high_to_low = sorted(marks, key=lambda x: x[1], reverse=True)
print("Sorted by Marks (High to Low):", sorted_high_to_low)
