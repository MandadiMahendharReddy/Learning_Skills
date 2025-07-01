# 🔒 CHALLENGE: Online Course Platform System

# 📌 REQUIREMENTS:
# 1. Create an abstract base class `Course` using ABC module
#    - Define abstract method: course_info()

# 2. Create two child classes `FreeCourse` and `PaidCourse` that inherit from `Course`
#    - Each should override course_info() and display different messages

# 3. Add encapsulation:
#    - Make course name and instructor private
#    - Provide methods to get/set them properly

# 4. Create a method enroll() in both child classes, but with different behavior (Polymorphism)
#    - FreeCourse: prints "Enrolled successfully, no payment needed!"
#    - PaidCourse: prints "Enrolled successfully after payment!"

# 5. Create objects of both classes and test:
#    - course_info()
#    - enroll()
#    - getting/setting course name using encapsulated method

# 💡 Example Output:
# Course: Python Basics by John
# Enrolled successfully, no payment needed!

# Course: Data Science Pro by Alice
# Enrolled successfully after payment!

from abc import ABC, abstractmethod

class Courses(ABC):
    def __init__(self, course, instructor):
        self.__course=course
        self.__instructor=instructor
    def get_course(self):
        return self.__course
    def get_instructor(self):
        return self.__instructor
    @abstractmethod
    def course_info(self):
        pass
class FreeCourse(Courses):
    def course_info(self):
        return f"Course: {self.get_course()} by {self.get_instructor()}"
    def enroll(self):
        return f"Enrolled successfully, no payment needed!"
class PaidCourse(Courses):
    def course_info(self):
        return f"Course: {self.get_course()} by {self.get_instructor()}"
    def enroll(self):
        return f"Enrolled successfully after payment!"
f=FreeCourse(course='Python Basics', instructor='Mahendhar')
p=PaidCourse(course='Django', instructor='Amar')
print(f.course_info())
print(f.enroll())
print(p.course_info())
print(p.enroll())
