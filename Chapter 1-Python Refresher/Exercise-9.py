# Create an int list with 10 values
my_list = [23, 7, 56, 12, 45, 9, 33, 18, 5, 27]

# Output the list using a for loop
print("Original List:")
for element in my_list:
    print(element, end=" ")
print()

# Output the highest and lowest value
max_value = max(my_list)
min_value = min(my_list)
print(f"Highest Value: {max_value}")
print(f"Lowest Value: {min_value}")

# Sort the elements in ascending order
my_list.sort()
print("Sorted in Ascending Order:", my_list)

# Sort the elements in descending order
my_list.sort(reverse=True)
print("Sorted in Descending Order:", my_list)

# Append two elements
my_list.append(42)
my_list.append(15)

# Print the list after appending
print("List after Appending Elements:", my_list)
