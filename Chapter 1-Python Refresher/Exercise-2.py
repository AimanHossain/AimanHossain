# Prompt the user for two integer inputs
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
if num2 != 0:
    quotient_result = num1 / num2
    remainder_result = num1 % num2
else:
    quotient_result = "Undefined (division by zero)"
    remainder_result = "Undefined (division by zero)"
print(f"Sum: {num1} + {num2} = {sum_result}")
print(f"Difference: {num1} - {num2} = {difference_result}")
print(f"Product: {num1} * {num2} = {product_result}")
print(f"Quotient: {num1} / {num2} = {quotient_result}")
print(f"Remainder: {num1} % {num2} = {remainder_result}")