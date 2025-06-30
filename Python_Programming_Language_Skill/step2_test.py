import requests

BASE_URL = "http://127.0.0.1:5000/todos"

# GET
print("All Todos:")
print(requests.get(BASE_URL).json())

# POST
new = {"title": "Practice Flask", "completed": False}
print("Added Todo:")
print(requests.post(BASE_URL, json=new).json())

# PUT
update = {"title": "Practice Flask - Updated", "completed": True}
print("Updated Todo:")
print(requests.put(BASE_URL + "/3", json=update).json())

# DELETE
print("Delete Todo:")
print(requests.delete(BASE_URL + "/3").json())
