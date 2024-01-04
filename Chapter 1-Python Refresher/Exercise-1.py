print("Hello, user!") 
name = input("What is your name? ").title()
age = int(input("What is your age? "))
name_length = len(name)
future_age = age + 1
print(f"It is good to meet you, {name}")
print("The length of your name is:")
print(name_length)
print(f"You will be {future_age} in a year.")