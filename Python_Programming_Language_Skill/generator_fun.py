def read_large_file(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            yield line

# Usage
for line in read_large_file('example.txt'):
    print(line.strip())

# Example: Fibonacci Generator using yield
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Use it
for num in fibonacci(5):
    print(num)  # Output: 0 1 1 2 3


