class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def info(self):
        return f"{self.name} is in grade {self.grade}."
# Create object
s1 = Student("Mahendhar", 10)
s2 = Student("Advait", 1)
# Call method
print(s1.info())  # Mahendhar is in grade 10.
print(s2.info())  # Advait is in grade 1.

