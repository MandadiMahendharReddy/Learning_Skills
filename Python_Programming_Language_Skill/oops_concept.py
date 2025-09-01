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


print("================================Challenge OOPS=======================================")

# OOP Challenge: Personal Finance Tracker (Income + Expenditure with Categories)

# 1. Abstraction:
# - Create an abstract class `Transaction` with:
#   - Private attributes: __amount, __description
#   - Abstract method: get_summary()
#   - Concrete method: get_amount() to return amount

# 2. Encapsulation:
# - Protect amount and description with __
# - Provide public getter methods for each

# 3. Inheritance &  4. Polymorphism:
# - Create two child classes:
#   1. `Income`: overrides get_summary() to print: "Income: ₹amount from [desc]"
#   2. `Expense`: overrides get_summary() to print: "Spent ₹amount on [desc]"

# - Also, add categories to Expense like "Food", "Bills", "Travel", etc.

# Test Code:
# - Create a list of transactions: some Income, some Expense
# - Print all transaction summaries
# - Calculate total income, total expenses, and balance
# - Show category-wise expense summary (optional bonus)

# Expected Output
# Income: ₹15000 from Freelancing
# Spent ₹500 on Food
# Spent ₹1000 on Bills
# Spent ₹2000 on Travel
# Total Income: ₹15000
# Total Expenses: ₹3500
# Balance: ₹11500


from abc import ABC, abstractmethod

# Abstraction: Base class that hides internal logic and defines common structure
class Transaction(ABC):
    def __init__(self, amount, description):
        self.__amount = amount  # Encapsulated (private) attribute
        self.__description = description

    def get_amount(self):
        return self.__amount  # Getter method for amount

    def get_description(self):
        return self.__description  # Getter method for description

    @abstractmethod
    def get_summary(self):
        pass  # Abstract method to be defined differently by child classes


# Inheritance + Polymorphism
class Income(Transaction):
    def get_summary(self):
        return f"Income: ₹{self.get_amount()} from {self.get_description()}"


class Expense(Transaction):
    def __init__(self, amount, description, category):
        super().__init__(amount, description)
        self.__category = category  # Encapsulated category

    def get_category(self):
        return self.__category

    def get_summary(self):
        return f"Spent ₹{self.get_amount()} on {self.get_description()} [{self.get_category()}]"


# Test Code Starts Here

# Create sample transactions
transactions = [
    Income(15000, "Freelance Project"),
    Expense(500, "Lunch", "Food"),
    Expense(1000, "Electricity Bill", "Utilities"),
    Expense(2000, "Train Ticket", "Travel"),
    Income(5000, "Bonus"),
    Expense(1500, "Groceries", "Food"),
    Expense(1000, "metro", "Travel"),
]

# Print all transaction summaries
print("All Transactions:\n")
for t in transactions:
    print(t.get_summary())

# Calculate totals
total_income = sum(t.get_amount() for t in transactions if isinstance(t, Income))
total_expense = sum(t.get_amount() for t in transactions if isinstance(t, Expense))
balance = total_income - total_expense

print("\nSummary:")
print("Total Income: ₹", total_income)
print("Total Expenses: ₹", total_expense)
print("Remaining Balance: ₹", balance)

# Bonus: Category-wise expense summary
print("\nCategory-wise Expense Breakdown:")
category_summary = {}
for t in transactions:
    if isinstance(t, Expense):
        cat = t.get_category()
        category_summary[cat] = category_summary.get(cat, 0) + t.get_amount()

for cat, amt in category_summary.items():
    print(f"- {cat}: ₹{amt}")

# All Transactions:
#
# Income: ₹15000 from Freelance Project
# Spent ₹500 on Lunch [Food]
# Spent ₹1000 on Electricity Bill [Utilities]
# Spent ₹2000 on Train Ticket [Travel]
# Income: ₹5000 from Bonus
# Spent ₹1500 on Groceries [Food]
#
# Summary:
# Total Income: ₹ 20000
# Total Expenses: ₹ 5000
# Remaining Balance: ₹ 15000
#
# Category-wise Expense Breakdown:
# - Food: ₹2000
# - Utilities: ₹1000
# - Travel: ₹2000

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
# Abstract Base Class
class Courses(ABC):
    def __init__(self, course, instructor):
        # Encapsulated attributes
        self.__course = course
        self.__instructor = instructor
    # Getters to access private attributes
    def get_course(self):
        return self.__course
    def get_instructor(self):
        return self.__instructor
    # Abstract method - must be implemented by subclasses
    @abstractmethod
    def course_info(self):
        pass
# Subclass for free courses
class FreeCourse(Courses):
    def course_info(self):
        return f"Course: {self.get_course()} by {self.get_instructor()}"
    def enroll(self):
        return "Enrolled successfully, no payment needed!"
# Subclass for paid courses
class PaidCourse(Courses):
    def course_info(self):
        return f"Course: {self.get_course()} by {self.get_instructor()}"
    def enroll(self):
        return "Enrolled successfully after payment!"
# Creating objects
f = FreeCourse(course='Python Basics', instructor='Mahendhar')
p = PaidCourse(course='Django', instructor='Amar')
# Displaying course info and enrollment status
print(f.course_info())
print(f.enroll())
print(p.course_info())
print(p.enroll())
