# Function to calculate the number of seconds in a day
def calculate_seconds_in_a_day(days):
    hours_in_a_day = 24
    minutes_in_an_hour = 60
    seconds_in_a_minute = 60

    total_seconds = days * hours_in_a_day * minutes_in_an_hour * seconds_in_a_minute
    return total_seconds

# Get user input for the number of days
try:
    num_days = float(input("Enter the number of days: "))
    if num_days < 0:
        print("Please enter a non-negative number of days.")
    else:
        # Call the function to calculate the number of seconds
        total_seconds = calculate_seconds_in_a_day(num_days)
        print(f"There are {total_seconds} seconds in {num_days} days.")
except ValueError:
    print("Invalid input. Please enter a numeric value for the number of days.")
