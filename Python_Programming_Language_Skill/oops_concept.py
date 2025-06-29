from abc import ABC, abstractmethod

# Abstraction: Defines the abstract User structure
class User(ABC):
    def __init__(self, name, email):
        # Encapsulation: Making name and email private
        self.__name = name
        self.__email = email

    @abstractmethod
    def access_portal(self):
        # Abstract method: Must be implemented by all derived classes
        pass

    def get_user_info(self):  # Instance method
        return f"User: {self.__name}, Email: {self.__email}"

    @staticmethod
    def platform_policy():  # Static method
        return "All users must follow the community guidelines."

    @classmethod
    def portal_type(cls):  # Class method
        return f"This is an {cls.__name__} portal."

# Inheritance: Student inherits from User
class Student(User):
    def __init__(self, name, email, course):
        super().__init__(name, email)
        self.course = course

    def access_portal(self):  # Polymorphism: method overriding
        return f"Student accessing course: {self.course}"

# Inheritance: Instructor inherits from User
class Instructor(User):
    def __init__(self, name, email, expertise):
        super().__init__(name, email)
        self.expertise = expertise

    def access_portal(self):  # Polymorphism: method overriding
        return f"Instructor managing subject: {self.expertise}"

# 🧪 Sample Usage
student = Student("Mahendhar", "mahendhar@example.com", "Python Programming")
instructor = Instructor("Ravi", "ravi@example.com", "AI & ML")

# Instance method (Encapsulated data access)
print(student.get_user_info())
print(instructor.get_user_info())

# Polymorphic behavior (method overriding)
print(student.access_portal())
print(instructor.access_portal())

# Class method (Used for general info about class type)
print(Student.portal_type())

# Static method (Platform rule - same for all users)
print(User.platform_policy())
