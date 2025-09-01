# 1. Conditional Statements (if-else)
# Real-Time Example 1: Login Validation
# Let's say you're creating a login system where the program checks the user's credentials.
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")
# Real-Time Example 2: Discount Eligibility
# In an e-commerce site, a user might receive a discount if their total amount is more than $100.
total_amount = 120
if total_amount > 100:
    print("You get a 10% discount!")
else:
    print("No discount available.")

# Real-Time Example of for loop 1: Print Numbers 1 to 5
for i in range(1, 6):
    print(i)
#Real-Time Example 2: Iterating Over a List of Students
students = ["Alice", "Bob", "Charlie"]
for student in students:
    print(f"Student: {student}")

# while Loop
# Real-Time While Example 1: Countdown Timer
count = 5
while count > 0:
    print(f"Time left: {count} seconds")
    count -= 1
# Real-Time Example 2: Waiting for User Input
user_input = ""
while user_input != "exit":
    user_input = input("Enter a command (type 'exit' to quit): ")
    print(f"You typed: {user_input}")

# break: Exits the loop.
for i in range(10):
    if i == 5:
        break  # Exits the loop when i is 5
    print(i)

# continue: Skips the current iteration and continues with the next one.
for i in range(10):
    if i == 3:
        continue  # Skips only 3 and continue
    print(i)

# pass: Does nothing; serves as a placeholder.
for i in range(3):
    pass  # Nothing happens in this loop