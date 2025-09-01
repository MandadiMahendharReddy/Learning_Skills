def calculate(a, b):
    result = a + b
    breakpoint()  # Python 3.7+ (same as pdb.set_trace())
    return result * 2

print(calculate(10, 5))
