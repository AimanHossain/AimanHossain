def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    else:
        return x / y

def modulus(x, y):
    if y == 0:
        return "Error: Cannot calculate modulus with zero divisor."
    else:
        return x % y

def calculator_menu():
    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")

        choice = input("Choose an operation (1 to 5): ")

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = modulus(num1, num2)

        print(f"Result: {result}")

        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

# Run the calculator menu
calculator_menu()
