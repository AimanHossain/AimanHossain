from datetime import datetime

def calculate_age(birth_date):
    today = datetime.now()
    birth_date = datetime.strptime(birth_date, "%m/%d/%Y")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    return age

def main():
    user_input = input("Enter your date of birth (MM/DD/YYYY): ")

    try:
        age = calculate_age(user_input)
        print(f"Your age is {age} years.")
    except ValueError:
        print("Invalid date format. Please use MM/DD/YYYY.")

if __name__ == "__main__":
    main()
