# 1. add(element)
# Adds a single element to the set.
s = {1, 2}
s.add(3)
print(s)  # {1, 2, 3}

# 2. update(iterable)
# Adds multiple elements (from list, tuple, etc).
s.update([4, 5])
print(s)  # {1, 2, 3, 4, 5}

# 3. remove(element)
# Removes the element. Throws error if not present.
s.remove(2)
print(s)  # {1, 3, 4, 5}


# 4. discard(element)
# Removes the element if it exists. No error if it doesn't.
s.discard(3)
s.discard(100)  # No error
print(s)

# 5. pop()
# Removes and returns a random item (since sets are unordered).
item = s.pop()
print("Removed:", item)
print(s)

# 6. clear()
# Removes all elements.
s.clear()
print(s)  # set()

# 7. union(set2)
# Returns a new set with all elements from both sets.
a = {1, 2}
b = {2, 3}
print(a.union(b))  # {1, 2, 3}

# 8. intersection(set2)
# Returns common elements in both sets.
print(a.intersection(b))  # {2}

# 9. difference(set2)
# Elements in set A but not in set B.
print(a.difference(b))  # {1}

# 10. symmetric_difference(set2)
# Elements in either set A or set B, but not both.
print(a.symmetric_difference(b))  # {1, 3}

# 11. copy()
# Returns a shallow copy of the set.
s={1,2,3,5,5,6}
s2 = s.copy()
print(s2)

