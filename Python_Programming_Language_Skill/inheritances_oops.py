print("==================================1. Single Inheritance=======================================")
# Single Inheritance
# Base Class
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    def show_details(self):
        return f"Employee: {self.name}, ID: {self.emp_id}, Salary: ₹{self.salary}"
    def get_annual_salary(self):
        return self.salary * 12
# Child Class (inherits from Employee)
class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)  # Call parent constructor
        self.department = department
    def show_details(self):
        base_info = super().show_details()
        return f"{base_info}, Department: {self.department}"

    def assign_task(self, task):
        return f"{self.name} (Manager of {self.department}) assigned task: {task}"
# Create Employee and Manager objects
emp1 = Employee("Ravi", 101, 50000)
mgr1 = Manager("Mahendhar", 201, 80000, "IT")
# Call methods
print(emp1.show_details())
print("Annual Salary:", emp1.get_annual_salary())

print(mgr1.show_details())
print("Annual Salary:", mgr1.get_annual_salary())
print(mgr1.assign_task("Complete project deployment"))
# Employee: Ravi, ID: 101, Salary: ₹50000
# Annual Salary: 600000
# Employee: Mahendhar, ID: 201, Salary: ₹80000, Department: IT
# Annual Salary: 960000
# Mahendhar (Manager of IT) assigned task: Complete project deployment
print("==================================2. multiple Inheritance=======================================")
#2. multiple: Real-Life Example: TeamLead inherits from both Developer and Tester
# Parent Class 1
class Developer:
    def write_code(self):
        return "Writing Python code..."

# Parent Class 2
class Tester:
    def test_code(self):
        return "Testing the application..."

# Child Class
class TeamLead(Developer, Tester):
    def manage_team(self):
        return "Managing the development and testing team."

lead = TeamLead()
print(lead.write_code())
print(lead.test_code())
print(lead.manage_team())
print("==================================3. Multilevel Inheritance=======================================")
#3. Multilevel Inheritance
# Real-Life Example: Intern → Employee → Person
# Base Class
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}."

# Derived Class 1
class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def show_id(self):
        return f"My employee ID is {self.emp_id}."

# Derived Class 2
class Intern(Employee):
    def __init__(self, name, emp_id, university):
        super().__init__(name, emp_id)
        self.university = university

    def show_university(self):
        return f"I am from {self.university} University."
intern = Intern("Rahul", 105, "IIT Madras")
print(intern.introduce())
print(intern.show_id())
print(intern.show_university())
# My name is Rahul.
# My employee ID is 105.
# I am from IIT Madras University.
print("==================================4. Hierarchical Inheritance=======================================")
#4. Hierarchical Inheritance
# Real-Life Example: Dog and Cat both inherit from Animal
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

# Child Class 1
class Dog(Animal):
    def bark(self):
        return f"{self.name} says: Woof!"

# Child Class 2
class Cat(Animal):
    def meow(self):
        return f"{self.name} says: Meow!"
dog = Dog("Tommy")
cat = Cat("Kitty")

print(dog.eat())
print(dog.bark())

print(cat.eat())
print(cat.meow())

# Tommy is eating.
# Tommy says: Woof!
# Kitty is eating.
# Kitty says: Meow!

print("=============================Challenge==================================")
# 🎯 Problem Statement

# You are building a system for a tech company. Design a class structure using inheritance:

# ✅ Base Class: Person
# Attributes: name, age
# Method: introduce()

# ✅ Level 1 Derived Class: Employee (Single Inheritance)
# Extra attribute: emp_id
# Method: show_id()

# ✅ Level 2 Derived Class: Developer (Multilevel Inheritance)
# Extra attribute: skills (list)
# Method: show_skills()

# ✅ Separate Class: Freelancer
# Attribute: projects
# Method: show_projects()

# ✅ Final Derived Class: RemoteDeveloper
# Inherits from Developer and Freelancer (Multiple Inheritance)
# Method: remote_status()

# ✅ Separate Derived Class from Person: HR (Hierarchical Inheritance)
# Extra attribute: department
# Method: show_department()

# 🔹 Create instances of RemoteDeveloper and HR
# 🔹 Show all relevant details using their methods
# 👨‍👩‍👧 Base Class (Used in Single, Multilevel, and Hierarchical Inheritance)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}"

# 🔹 SINGLE INHERITANCE: Employee inherits from Person
class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id

    def show_id(self):
        return f"My employee ID is {self.emp_id}"

# 🔹 MULTILEVEL INHERITANCE: Developer inherits from Employee -> Person
class Developer(Employee):
    def __init__(self, name, age, emp_id, skills):
        super().__init__(name, age, emp_id)
        self.skills = skills

    def show_skills(self):
        return f"I am good at these skills: {self.skills}"

# 🔹 Standalone Class (used in Multiple Inheritance)
class Freelancer:
    def __init__(self, projects):
        self.projects = projects

    def show_projects(self):
        return f"I have worked on these projects: {self.projects}"

# 🔹 MULTIPLE INHERITANCE: RemoteDeveloper inherits from Developer and Freelancer
class RemoteDeveloper(Developer, Freelancer):
    def __init__(self, name, age, emp_id, skills, projects):
        Developer.__init__(self, name, age, emp_id, skills)
        Freelancer.__init__(self, projects)

    def remote_status(self):
        return f"I work remotely on projects: [{self.projects}]"

# 🔹 HIERARCHICAL INHERITANCE: HR also inherits from Person (like Employee does)
class HR(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def show_department(self):
        return f"I belong to the {self.department} department"


# 🧪 Test Area (Instances and Outputs)
rt = RemoteDeveloper(name="Mahendhar", age=33, emp_id=1234, skills="Python, Django", projects="TPM")
hr = HR(name="Radhika", age=23, department="HR")

print(rt.introduce())           # From Person
print(rt.show_id())             # From Employee
print(rt.show_skills())         # From Developer
print(rt.show_projects())       # From Freelancer
print(rt.remote_status())       # Own method

print(hr.introduce())           # From Person
print(hr.show_department())     # From HR