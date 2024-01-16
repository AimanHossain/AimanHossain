staff = ["Arshiya", "Usman", "Iftikhar", "Usman", "Rafia", "Mary", "Anmol", "Zainab", "Iftikhar", "Arshiya", "Rafia", "Jake"]

# Create an empty dictionary to store the count of each item
item_count = {}

# Count the number of times each item appears in the list
for item in staff:
    if item in item_count:
        item_count[item] += 1
    else:
        item_count[item] = 1

# Display the count for each item
for item, count in item_count.items():
    print(f"{item}: {count} times")
