#1. Instance Method
class Student:
    def __init__(self, name):
        self.name = name
    def greet(self):  # Instance method
        return f"Hello, {self.name}!"
s1 = Student("Mahendhar")   # Create object
print(s1.greet())           # Call instance method using object

#2. Class Method
class Employee:
    company = "Google"
    @classmethod
    def change_company(cls, new_name):  # Class method
        cls.company = new_name
Employee.change_company("TCS")     # Call using class name
print(Employee.company)            # Output: TCS

#3.Static Method
class MathUtils:
    @staticmethod
    def add(a, b):  # Static method
        return a + b
print(MathUtils.add(10, 5))   # Call using class name

# using all methods
class BankAccount:
    bank_name = "SBI"
    interest_rate = 0.05  # 5% interest for all accounts

    def __init__(self, customer_name, balance):
        self.customer_name = customer_name
        self.balance = balance

    # ✅ Instance Method – works with object-specific data
    def show_balance(self):
        return f"{self.customer_name}'s balance: ₹{self.balance}"

    # ✅ Class Method – modifies class-level data
    @classmethod
    def update_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        return f"New interest rate set to {cls.interest_rate * 100}%"

    # ✅ Static Method – helper that doesn’t need object/class data
    @staticmethod
    def validate_deposit(amount):
        return amount > 0
# Create account (Instance)
acc1 = BankAccount("Mahendhar", 10000)

# Instance Method → Specific to this user
print(acc1.show_balance())
# Output: Mahendhar's balance: ₹10000

# Static Method → Validate deposit (common utility)
print(BankAccount.validate_deposit(500))
# Output: True

# Class Method → Bank manager changes interest rate for all
print(BankAccount.update_interest_rate(0.07))
# Output: New interest rate set to 7.0%

print("================================Challenge======================================")

# 💡 Challenge: Library Management System

# 1. Create a class called LibraryBook

# 2. Each book should have the following attributes:
#    - title (string)
#    - author (string)
#    - isbn (string of digits)

# 3. Create an instance method:
#    - display_info(self)
#    - Should print the book's title and author in a friendly format

# 4. Create a class method:
#    - set_library_name(cls, name)
#    - Should set or update the library name for all books

# 5. Create a static method:
#    - is_valid_isbn(isbn)
#    - Should return True if the ISBN is exactly 13 digits long, otherwise False

# 6. Create two book objects using the class

# 7. Use the instance method to display book info

# 8. Use the static method to validate each book's ISBN

# 9. Use the class method to update and show the library name

# Example Data to Use:
# book1 = LibraryBook("Bhagavad Gita", "Vyasa", "9781234567890")
# book2 = LibraryBook("Python Basics", "Mahendhar", "123456")

# 🎯 Goal:
# Practice using instance, class, and static methods in a real-world scenario!

class LibraryBook:
    library_name = "Ambedkar study circle"
    def __init__(self, title, author, isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display_info(self):
        return f"'{self.title}' written by {self.author} with ISBN {self.isbn}"
    @classmethod
    def set_library_name(cls, new_name):
        print(f"Current Library: {LibraryBook.library_name}")
        cls.library_name = new_name
        return f"Updated library name to {cls.library_name}"
    @staticmethod
    def is_valid_isbn(isbn):
        if len(isbn) == 13:
            return True
        else:
            return False


book1= LibraryBook("Bhagavad Gita", "Vyasa", "9781234567890")
book2 = LibraryBook("Python Basics", "Mahendhar", "123456")
print(book1.display_info())
print(LibraryBook.set_library_name("Gandhi library"))
print(LibraryBook.is_valid_isbn("9781234567890"))
print(book2.display_info())
print(LibraryBook.set_library_name("Ram library"))
print(LibraryBook.is_valid_isbn("123456"))

