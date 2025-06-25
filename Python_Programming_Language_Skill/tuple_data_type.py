# Syntax: person = ('John', 25, 'Engineer'), my_tuple = (1, "hello", 3.14)
# t = (5,)   valid 1-item tuple

# 1. count(value):
t = (1, 2, 2, 3, 2)
print(t.count(3))  # Output: 1

# 2.index(value):
t = ("a", "b", "c", "a")
print(t.index("a"))  # Output: 0
#print(t.index("d"))  # ValueError

# 3.Unapacking tuple
person = ("Mahendhar", 25, "India")
name, age, country = person
print(name)   # Mahendhar

# Return multiple values from a function:
def get_user():
    return ("Mahendhar", 27)
name, age = get_user()
print(name)  # Mahendhar
