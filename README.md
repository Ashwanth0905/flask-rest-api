# Flask REST API - User Manager

This is a simple REST API created using Python and Flask. It lets you manage user data with basic operations like adding, viewing, updating, and deleting users. The data is stored in memory (not in a database).

---

## 🔧 Features

- View all users (`GET /users`)
- Add a new user (`POST /users`)
- Update user by ID (`PUT /users/<id>`)
- Delete user by ID (`DELETE /users/<id>`)

---

## 🛠️ Requirements

- Python
- Flask

---

## ▶️ How to Run

1. Open terminal and go to your project folder.

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate    # For Windows
   source venv/bin/activate # For Mac/Linux
   pip install -r requirements.txt
   python app.py
   http://127.0.0.1:5000/users


