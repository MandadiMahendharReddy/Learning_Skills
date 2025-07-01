from abc import ABC, abstractmethod

# Abstraction: Base abstract class for any Task Manager
class TaskManager(ABC):
    def __init__(self):
        self._tasks = []  # Encapsulation: Task list is protected

    @abstractmethod
    def display_tasks(self):
        pass

    def add_task(self, task):
        self._tasks.append({'task': task, 'completed': False})
        print(self._tasks)
        print(f"Task added: {task}")

    def complete_task(self, index):
        if 0 <= index < len(self._tasks):
            self._tasks[index]['completed'] = True
            print(f"Task {index + 1} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self._tasks):
            deleted = self._tasks.pop(index)
            print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task number.")

# Inheritance + Polymorphism
class UserManager(TaskManager):
    def display_tasks(self):
        print("\nYour To-Do List:")
        print(self._tasks)
        if not self._tasks:
            print("No tasks found.")
        else:
            for i, t in enumerate(self._tasks):
                status = "✔️" if t['completed'] else "❌"
                print(f"{i + 1}. {t['task']} [{status}]")

# Another child class with admin-style view (polymorphism)
class AdminManager(TaskManager):
    def display_tasks(self):
        print("\n🔐 Admin Task View:")
        if not self._tasks:
            print("No tasks available.")
        else:
            for i, t in enumerate(self._tasks):
                status = "Completed" if t['completed'] else "Pending"
                print(f"{i + 1}. Task: {t['task']} | Status: {status}")
# Choose which type of user (UserManager or AdminManager)
user_type = input("Login as (user/admin): ").strip().lower()

manager = UserManager() if user_type == "user" else AdminManager()

while True:
    print("\n--- TO-DO MENU ---")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Delete Task")
    print("4. View Tasks")
    print("5. Exit")

    choice = input("Enter choice (1-5): ").strip()

    if choice == "1":
        task = input("Enter task: ")
        manager.add_task(task)
    elif choice == "2":
        index = int(input("Task number to complete: ")) - 1
        manager.complete_task(index)
    elif choice == "3":
        index = int(input("Task number to delete: ")) - 1
        manager.delete_task(index)
    elif choice == "4":
        manager.display_tasks()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")
