def sum_of_digits(number):
    # Convert the number to a string to iterate through each digit
    digits = [int(digit) for digit in str(number)]
    return sum(digits)

# Get user input for the number
try:
    user_number = int(input("Enter a number: "))
    if user_number < 0:
        print("Please enter a non-negative number.")
    else:
        # Call the function to calculate the sum of digits
        result = sum_of_digits(user_number)
        print(f"The sum of digits in {user_number} is: {result}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
