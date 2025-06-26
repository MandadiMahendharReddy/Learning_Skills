# Example: Simple Iterator
nums = [1, 2, 3]
itr = iter(nums)  # Get iterator
print(next(itr))  # 1
print(next(itr))  # 2
print(next(itr))  # 3
# print(next(itr))  # ❌ StopIteration error

# Iterating Through a File (Line by Line)
file = open('example.txt', 'r')
file_iterator = iter(file)

for line in file_iterator:
    print(line.strip())

class Countdown:
    def __init__(self, start):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        current = self.num
        self.num -= 1
        return current

# Use it
for i in Countdown(5):
    print(i)

