def add(a, b):
    return a + b
result = add(10, 5)
print(result)  # Output: 15


# Tuple return
def operations(a, b):
    return a + b, a * b

s, p = operations(3, 4)
print(s, p)  # Output: 7 12

# Once a return is executed, the function ends. Any code after it is ignored.
# You cannot return multiple times in one function call
# Wrong return placement or value can cause silent bugs.
def check(value):
    return  # exits early
    print("This won't print")  # unreachable code
