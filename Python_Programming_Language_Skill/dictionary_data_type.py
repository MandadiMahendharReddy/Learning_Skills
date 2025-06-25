# 1.get(key, default):
# Returns the value of the key. If the key doesn’t exist, it returns default.
user = {"name": "Krishna"}
print(user.get("name"))          # Krishna
print(user.get("age", "Unknown"))  # Unknown
print(user.get("age"))  # None

# 2.keys()
# Returns all the keys in the dictionary.
print(user.keys())  # dict_keys(['name'])

# 3.values()
# Returns all the values.
print(user.values())  # dict_values(['Krishna'])

# 4.items()
# Returns all key-value pairs as tuples.
for key, value in user.items():
    print(key, value)
# name Krishna

# 5.update(new_dict)
# Adds or updates key-value pairs from another dictionary.
user.update({"age": 30})
print(user)  # {'name': 'Krishna', 'age': 30}

# 6.pop(key)
# Removes a key and returns its value.
age = user.pop("age")
print(age)     # 30
print(user)    # {'name': 'Krishna'}

# 7.popitem()
# Removes and returns the last inserted key-value pair.
user = {"a": 1, "b": 2}
print(user.popitem())  # ('b', 2)

# 8.clear()
# Removes all items from the dictionary.
user.clear()
print(user)  # {}

# 9.copy()
# Returns a shallow copy of the dictionary.
d1 = {"x": 1}
d2 = d1.copy()
d1["x"] = 10
print(d2["x"])  # 1 (original copy safe)

# 10.setdefault(key, default)
# Returns the value of key;
# if the key doesn’t exist, add it with the default value.
settings = {}
settings.setdefault("theme", "dark")
print(settings)  # {'theme': 'dark'}

# 11. Dictionary Comprehension:
squares = {x: x*x for x in range(1, 4)}
print(squares)  # {1: 1, 2: 4, 3: 9}

