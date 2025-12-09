
# 📌 Flask REST API with CRUD + Built-in Web UI

This project is a simple **Flask-based REST API** that performs CRUD (Create, Read, Update, Delete) operations on a list of users.  
It includes a **user-friendly HTML UI** for interacting with the API directly from the browser.

---

## 🚀 Features

### ✔ REST API Endpoints
- **GET /users** → Fetch all users  
- **POST /users** → Add a new user  
- **PUT /users/<id>** → Update an existing user  
- **DELETE /users/<id>** → Delete a user by ID  

### ✔ Built-in Web Interface
- Add new users  
- Update existing users  
- Delete users  
- View user list  
- Success & error messages  
- Clean and responsive UI  

### ✔ Fake In-Memory Database
A simple Python list acts as a temporary database:
```python
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]
````

---

## 🛠 Tech Stack

* **Python 3**
* **Flask**
* **HTML + CSS + JavaScript (embedded UI)**

---

## 📂 Project Structure

```
├── app.py        # Main Flask application
├── README.md     # Project documentation
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/flask-rest-api.git
cd flask-rest-api
```

### 2️⃣ Install Dependencies

```bash
pip install flask
```

### 3️⃣ Run the App

```bash
python app.py
```

### 4️⃣ Open in Browser

Visit:

```
http://127.0.0.1:5000/
```

You will see the interactive UI where you can add, update, delete, and view users.

---

## 🧪 API Usage Examples

### **GET — Fetch All Users**

```bash
GET /users
```

Response:

```json
[
  { "id": 1, "name": "Alice" },
  { "id": 2, "name": "Bob" }
]
```

---

### **POST — Add a User**

```bash
POST /users
Content-Type: application/json

{
  "name": "John"
}
```

Response:

```json
{ "id": 3, "name": "John" }
```

---

### **PUT — Update a User**

```bash
PUT /users/1
Content-Type: application/json

{
  "name": "Alice Updated"
}
```

---

### **DELETE — Delete a User**

```bash
DELETE /users/1
```

Response:

```json
{ "message": "User deleted" }
```

---

## 🎨 UI Overview

The application includes:

* Form-based user actions
* Automatic user list updates
* Styled UI with HTML + CSS
* JSON display for API responses

---

## 🎯 Learning Objectives

This project helps you understand:

* How Flask handles routes
* How REST APIs are built
* How frontend interacts with backend using `fetch()`
* How to send and receive JSON
* Basics of CRUD operations

---

## 🤝 Contributing

Feel free to open issues or submit pull requests to improve the project.

---

## 📄 License

This project is open-source under the **MIT License**.

```
