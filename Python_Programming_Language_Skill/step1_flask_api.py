from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database (in-memory)
todos = [
    {"id": 1, "title": "Learn Python", "completed": False},
    {"id": 2, "title": "Build API", "completed": False}
]

# GET – Fetch all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# POST – Add a new todo
@app.route('/todos', methods=['POST'])
def add_todo():
    new_todo = request.get_json()
    new_todo["id"] = len(todos) + 1
    todos.append(new_todo)
    return jsonify(new_todo), 201

# PUT – Update a todo
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    for todo in todos:
        if todo["id"] == todo_id:
            todo.update(data)
            return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404

# DELETE – Delete a todo
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return jsonify({"message": "Deleted successfully"})
    return jsonify({"error": "Todo not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
