# Given list
locations = ['dubai', 'paris', 'switzerland', 'London', 'amsterdam', 'New York']

# Print the original list and find its length
print("Original List:", locations)
print("Length of the list:", len(locations))

# Use sorted() to print the list in alphabetical order without modifying the actual list
sorted_list_alpha = sorted(locations)
print("Sorted List (Alphabetical):", sorted_list_alpha)

# Print the original list to show it is still in its original order
print("Original List (Unmodified):", locations)

# Use sorted() to print the list in reverse alphabetical order without modifying the actual list
sorted_list_reverse_alpha = sorted(locations, reverse=True)
print("Sorted List (Reverse Alphabetical):", sorted_list_reverse_alpha)

# Print the original list to show it is still in its original order
print("Original List (Unmodified):", locations)

# Use reverse() to change the order of the list
locations.reverse()
print("Reversed List:", locations)

# Use sort() to change the list so it’s stored in alphabetical order
locations.sort()
print("Sorted List (Alphabetical):", locations)

# Use sort() to change the list so it’s stored in reverse alphabetical order
locations.sort(reverse=True)
print("Sorted List (Reverse Alphabetical):", locations)
