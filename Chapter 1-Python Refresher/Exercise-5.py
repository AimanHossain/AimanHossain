count = 0

while True:
    user_input = input("Do you want to continue? (Y/N): ")
    
    if user_input.upper() == 'Y':
        count += 1
    elif user_input.upper() == 'N':
        break
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")

print(f"The while loop executed {count} times.")
