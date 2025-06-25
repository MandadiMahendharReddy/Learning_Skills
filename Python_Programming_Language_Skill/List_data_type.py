# 1. append()
# Adds an element to the end of the list.
fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)  # ['apple', 'banana', 'cherry']
# Use case: Adding items to a shopping cart.

# 2. extend()
# Adds multiple elements to the end of the list.
fruits = ['apple', 'banana']
fruits.extend(['Grapes', 'mango', 'watermelon'])
print(fruits)  # ['apple', 'banana', 'Grapes', 'mango', 'watermelon']
# Use case: Merging two lists.

# 3. insert(‘index’, ‘item’)
# Inserts an element at a specific position.
fruits = ['apple', 'cherry']
fruits.insert(1, 'grapes')
print(fruits)  # ['apple', 'grapes', 'cherry']
# Use case: Insert priority task at the top.

# 4. remove(‘item’)
# Removes the first matching element.
fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits)  # ['apple', 'cherry']
# Use case: Remove specific user entry.

# 5. pop()
# Removes and returns element at the given index (default is last).
fruits = ['apple', 'banana', 'cherry']
last_item = fruits.pop()
print(last_item)  # cherry
print(fruits)
# Use case: Undo last operation.

# 6. clear()
# Removes all elements from the list.
fruits = ['apple', 'banana']
fruits.clear()
print(fruits)  # []
# Use case: Reset a list after submission.

# 7. index('item')
# Returns the first index of the specified value.
fruits = ['apple', 'banana', 'cherry']
print(fruits.index('banana'))  # 1
# Use case: Find position of item in ordered menu.

# 8. count()
# Returns number of times a value appears.
nums = [1, 2, 2, 3]
print(nums.count(2))  # 2
# Use case: Count votes in a list.

# 9. sort()
# Sorts the list in ascending order (in-place).
nums = [3, 1, 2]
nums.sort()
print(nums)  # [1, 2, 3]
# Use case: Rank leaderboard scores.
# Use sort(reverse=True) for descending.

# 10. sorted()
# Returns a new sorted list (does not modify original).
nums = [3, 1, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # [1, 2, 3]
# Use case: Display sorted results without changing actual order.

# 11. reverse()
# Reverses the list in-place.
nums = [1, 2, 3]
nums.reverse()
print(nums)  # [3, 2, 1]
# Use case: Show recent activities.

# 12. copy()
# Returns a shallow copy of the list.
original = [1, 2, 3]
copy_list = original.copy()
# Use case: Clone current state before changes.

#13 shallow copy and deep copy
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

print('original', original)
print('shallow', shallow)
print('deep', deep)

original[0][0] = 99

print('original', original)
print('shallow', shallow)
print('deep', deep)
