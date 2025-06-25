# factorial task
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# Use memoization or dynamic programming for optimizing recursive calls (e.g., Fibonacci).
# Example: Fibonacci with Recursion and computes the nth Fibonacci number where
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(6))  # Output: 8
