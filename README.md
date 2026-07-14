# 📋 TaskFlow

TaskFlow is a modern task management web application built with **Python**, **Flask**, **SQLAlchemy**, **HTML**, and **CSS**. It helps users organize their daily tasks through a clean, responsive interface while demonstrating secure authentication and CRUD operations.

---

## ✨ Features

### 🔐 User Authentication

* User registration
* Secure login and logout
* Password hashing with Werkzeug
* Session management
* Email uniqueness validation
* Strong password validation
* Flash messages for user feedback

### ✅ Task Management

* Create tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Due dates
* Priority levels (High, Medium, Low)
* Task statistics dashboard

### 🎨 User Interface

* Responsive design for desktop, tablet, and mobile
* Black and pink custom theme
* Professional dashboard
* Navigation bar
* Custom 404 and 500 error pages

---

## 🛠️ Technologies Used

### Backend

* Python 3
* Flask
* Flask-SQLAlchemy
* SQLite
* Werkzeug

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Development Tools

* Git
* GitHub
* Visual Studio Code

---

## 📂 Project Structure

```text
TaskFlow/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   ├── user.py
│   └── task.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── 404.html
│   └── 500.html
│
└── instance/
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/TaskFlow.git
```

Open the project:

```bash
cd TaskFlow
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## 🔒 Security Features

* Passwords are securely hashed before storage.
* Duplicate email registration is prevented.
* Email addresses are validated.
* Passwords must meet strength requirements.
* Session-based authentication protects user access.

---

## 📱 Responsive Design

TaskFlow is optimized for:

* 💻 Desktop
* 📱 Mobile
* 📲 Tablet

---

## 🎯 Future Improvements

* Edit tasks
* Search and filter tasks
* Categories
* Calendar view
* User profile page
* Email verification
* Password reset
* Notifications
* PostgreSQL database
* Dark/Light mode switch
* Premium subscription

---

## 👩‍💻 Author

**Hanin Atwi**

Computer Science Student at FIAP

GitHub: https://github.com/haninatwi0

LinkedIn: https://linkedin.com/in/haninatwi

---

## 📄 License

This project was developed for educational purposes and portfolio demonstration.
