def greet():
    message = "Hello!"  # 1. Local variable
    print(message)
greet()  # Output: Hello!
# print(message)  # This will give an error (variable is not accessible, NameError: name 'message' is not defined)




# Example of 2. Global Variable:
x = 100  # Global variable
def display():
    print(x)  # Accessing global variable
display()  # Output: 100
print(x)
# Modifying a Global Variable Inside a Function:
y = 50  # Global variable
def modify():
    global y  # Declaring global variable
    y = 200
modify()
print(y)  # Output: 200


# Example of 3. Instance Variable:
class Car:
    def __init__(self, brand):
        self.brand = brand  # Instance variable
car1 = Car("Toyota")
car2 = Car("Honda")
print(car1.brand)  # Output: Toyota
print(car2.brand)  # Output: Honda


# Example of 3. Class Variable:
class Employee:
    company = "Google"  # Class variable
emp1 = Employee()
emp2 = Employee()
print(emp1.company)  # Output: Google
print(emp2.company)  # Output: Google
# Modifying class variable
Employee.company = "Microsoft"
print(emp1.company)  # Output: Microsoft
print(emp2.company)  # Output: Microsoft


# Example of 4. Constants:
PI = 3.14159  # Constant (by convention)
def area(radius):
    return PI * radius * radius
print(area(5))  # Output: 78.53975


# Example of 5. Argument variable
def my_function(a, b=10, *args, d, **kwargs):
    print(f"Positional: {a}")
    print(f"Default: {b}")
    print(f"Variable Positional (*args): {args}")
    print(f"Keyword-Only: {d}")
    print(f"Variable Keyword (**kwargs): {kwargs}")

# Calling the function
# Order: positional → default → *args → keyword-only → **kwargs
my_function(1, 2, 3, 4, d=5, f=6, g=7)

