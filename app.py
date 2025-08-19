from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Fake database
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# Home page with styled UI
@app.route('/')
def home():
    return render_template_string('''
        <html>
        <head>
            <title>Flask REST API</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background: #f9f9f9; }
                h1 { color: #2c3e50; }
                h2 { margin-top: 30px; color: #34495e; }
                form, .box { margin-bottom: 20px; padding: 15px; background: #fff; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
                input, button { padding: 8px; margin: 5px; border-radius: 5px; border: 1px solid #ccc; }
                button { background: #3498db; color: white; border: none; cursor: pointer; }
                button:hover { background: #2980b9; }
                #usersList, #message { margin-top: 20px; }
                pre { background: #eee; padding: 10px; border-radius: 5px; }
                .success { color: green; font-weight: bold; }
                .error { color: red; font-weight: bold; }
            </style>
        </head>
        <body>
            <h1>Build REST API using Flask</h1>

            <div id="message"></div>

            <!-- Add User -->
            <h2>Add User</h2>
            <form onsubmit="addUser(event)">
                <input type="text" id="addName" placeholder="Enter name" required>
                <button type="submit">Add User</button>
            </form>

            <!-- Update User -->
            <h2>Update User</h2>
            <form onsubmit="updateUser(event)">
                <input type="number" id="updateId" placeholder="User ID" required>
                <input type="text" id="updateName" placeholder="New Name" required>
                <button type="submit">Update User</button>
            </form>

            <!-- Delete User -->
            <h2>Delete User</h2>
            <form onsubmit="deleteUser(event)">
                <input type="number" id="deleteId" placeholder="User ID" required>
                <button type="submit">Delete User</button>
            </form>

            <!-- View Users -->
            <h2>Users List</h2>
            <button onclick="getUsers()">Show Users</button>
            <div id="usersList"></div>

            <script>
                function showMessage(text, type="success") {
                    let msgDiv = document.getElementById("message");
                    msgDiv.innerHTML = '<p class="' + type + '">' + text + '</p>';
                    setTimeout(() => { msgDiv.innerHTML = ""; }, 3000); // Auto-clear in 3 sec
                }

                async function getUsers() {
                    let res = await fetch('/users');
                    let data = await res.json();
                    document.getElementById("usersList").innerHTML = "<pre>" + JSON.stringify(data, null, 2) + "</pre>";
                    # showMessage("Users fetched successfully!");
                }

                async function addUser(event) {
                    event.preventDefault();
                    let name = document.getElementById("addName").value;
                    let res = await fetch('/users', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ name })
                    });
                    if (res.ok) {
                        document.getElementById("addName").value = ""; // clear input
                        getUsers();
                        showMessage("User added successfully!");
                    } else {
                        showMessage("Failed to add user.", "error");
                    }
                }

                async function updateUser(event) {
                    event.preventDefault();
                    let id = document.getElementById("updateId").value;
                    let name = document.getElementById("updateName").value;

                    let res = await fetch('/users/' + id, {
                        method: 'PUT',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ name })
                    });
                    if (res.ok) {
                        document.getElementById("updateId").value = "";
                        document.getElementById("updateName").value = "";
                        getUsers();
                        showMessage("User updated successfully!");
                    } else {
                        let err = await res.json();
                        showMessage(err.error, "error");
                    }
                }

                async function deleteUser(event) {
                    event.preventDefault();
                    let id = document.getElementById("deleteId").value;

                    let res = await fetch('/users/' + id, { method: 'DELETE' });
                    if (res.ok) {
                        document.getElementById("deleteId").value = "";
                        getUsers();
                        showMessage("User deleted successfully!");
                    } else {
                        let err = await res.json();
                        showMessage(err.error, "error");
                    }
                }
            </script>
        </body>
        </html>
    ''')

# API endpoints
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400
    new_user = {"id": len(users) + 1, "name": data["name"]}
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id <= 0 or user_id > len(users):
        return jsonify({"error": "Invalid user ID"}), 400

    data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user["name"] = data.get("name", user["name"])
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    if user_id <= 0 or user_id > len(users):
        return jsonify({"error": "Invalid user ID"}), 400

    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
