# 1. Real-Time Example (GET Request - Public API):
import requests

# Example: Fetch current info about a public API
response = requests.get("https://api.agify.io/?name=mahendhar")

if response.status_code == 200:
    data = response.json()  # Convert JSON response to Python dict
    print("Name:", data["name"])
    print("Predicted Age:", data["age"])
    print("Number of Records:", data["count"])
else:
    print("Failed to retrieve data. Status code:", response.status_code)

# 2. Using POST with JSON Data:
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "Python API Example",
    "body": "This is a test post.",
    "userId": 101
}

headers = {'Content-type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers)

print("Status:", response.status_code)
print("Response JSON:", response.json())

# 3. PUT – Update existing data
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/1"
updated_data = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated content of the post",
    "userId": 1
}

response = requests.put(url, data=json.dumps(updated_data), headers={"Content-Type": "application/json"})
print("PUT:", response.json())

# 4. DELETE – Delete a record
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)
print("DELETE Status Code:", response.status_code)  # Should be 200

# Real time example to cover all HTTP methods

import requests

def get_tasks():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks = response.json()[:5]  # Just get first 5 for display
    print("Your Tasks:")
    for task in tasks:
        print(f"ID: {task['id']} | Title: {task['title']} | Completed: {task['completed']}")
def add_task(title):
    data = {
        "userId": 1,
        "title": title,
        "completed": False
    }
    response = requests.post("https://jsonplaceholder.typicode.com/todos", json=data)
    print("Task Created:", response.json())
def update_task(task_id, new_title):
    updated_data = {
        "userId": 1,
        "id": task_id,
        "title": new_title,
        "completed": True
    }
    response = requests.put(f"https://jsonplaceholder.typicode.com/todos/{task_id}", json=updated_data)
    print("Task Updated:", response.json())
def delete_task(task_id):
    response = requests.delete(f"https://jsonplaceholder.typicode.com/todos/{task_id}")
    if response.status_code == 200:
        print(f"Task {task_id} deleted successfully!")
    else:
        print("Failed to delete.")

get_tasks()
add_task("Complete Python OOPs")
update_task(1, "Updated: Finish Python Decorators")
delete_task(1)