def decorator_func(func):
    def wrapper():
        print("Before function call")
        #greet() #RecursionError: maximum recursion depth exceeded, # 🚫 Calls the function by its name, not using the parameter
        func()
        print("After function call")
    return wrapper
@decorator_func
def greet():
    print("Hello!")
greet()

# Decorator with Arguments Example:
def multiply_by(n):
    def decorator(func):
        print(n)
        def wrapper(x):
            print(x)
            return func(x) * n
        return wrapper
    return decorator

@multiply_by(3)
def get_number(x):
    return x
print(get_number(6))

@multiply_by(3)
def su_number(x):
    return x*x
print(su_number(6))

# even number decorator function validation
def only_even_args(func):     # 🧙 Decorator takes the real function (like add)
    def wrapper(a, b):        # 🛡️ New function with a guard inside
        if a % 2 == 0 and b % 2 == 0:
            return func(a, b) # ✅ Let the original function run
        else:
            return "Only even numbers are allowed!"  # ❌ Block
    return wrapper            # 🪄 Return the new version of the function

@only_even_args               # 🎯 Python replaces add = wrapper
def add(a, b):
    return a + b

print(add(2, 4))              # Actually runs wrapper(2, 4)
print(add(4, 9))              # Actually runs wrapper(4, 9)


# login access
def authenticate(func):
    user_logged_in = False
    def wrapper(user_logged_in):
        if user_logged_in == False:
            return "Access Denied. Please log in."
        else:
            return func(user_logged_in)
    return wrapper
@authenticate
def show_dashboard(user_logged_in):
    return "Welcome to your dashboard!"
print(show_dashboard(user_logged_in=True))

