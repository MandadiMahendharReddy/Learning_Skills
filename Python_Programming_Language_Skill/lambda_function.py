#Syntax: lambda arguments: expression
square = lambda x: x * x
print(square(5))  # Output: 25
#Same as:
def square(x):
    return x * x
print(square(5))

# map(function, iterable)
nums = [1, 2, 3]
result = list(map(lambda x: x * 2, nums))
print(result)  # [2, 4, 6]

# filter(function, iterable)
nums = [1, 2, 3, 4]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2, 4]

# sorted(iterable, key=..., reverse=False)
names = ['zara', 'adam', 'bob']
print(sorted(names))  # ['adam', 'bob', 'zara']
data = [(1, 'b'), (2, 'a'), (3, 'c')]
print(sorted(data, key=lambda x: x[1]))  # [(2, 'a'), (1, 'b'), (3, 'c')]
# Common Use Case Together:
students = [{'name': 'John', 'score': 85}, {'name': 'Emma', 'score': 92}]
top_students = list(filter(lambda s: s['score'] > 90, students))
print(top_students)  # [{'name': 'Emma', 'score': 92}]





