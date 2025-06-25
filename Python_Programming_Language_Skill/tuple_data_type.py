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


# Challenge
# 🛠️ TASKS (Use tuple methods and features):
# Print the student’s full record neatly.
# Access the name and branch using indexing.
# Convert tuple to list, update the branch to "AI & DS", then convert it back to tuple.
# Add a new field to tuple: "Passed" (Note: Tuples are immutable, so think smartly).
# Count how many times 2025 appears in the tuple.
# Find the index of "Computer Science" in the original tuple.
# Slice the tuple to only show the first 3 fields.
# Print the length of the final tuple.
# Loop through all items and print one by one.
# Use type() to confirm it’s a tuple.

def student_data(student):
    print(student)
    print(student[0], student[2])
    student = list(student)
    student[2] = "AI & DS"
    student=tuple(student)
    print(student)
    student=list(student)
    student.append("Passed")
    student=tuple(student)
    print(student)
    print(student.count(2025))
    student1 = ('Mahendhar', 101, 'Computer Science', 2025)
    print(student1.index('Computer Science'))
    print(student1[0:3])
    print(len(student))
    for i in student:
        print(i)
    print(type(student))

student = ("Mahendhar", 101, "Computer Science", 2025)
student_data(student)