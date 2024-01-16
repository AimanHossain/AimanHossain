def calculate_product(lst):
    product = 1
    for value in lst:
        product *= value
    return product

# Example list
my_list = [2, 3, 5, 7, 11, 13]

# Call the function and print the result
result = calculate_product(my_list)
print(f"The product of the list values is: {result}")
