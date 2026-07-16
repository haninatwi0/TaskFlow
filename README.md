# 📋 TaskFlow

TaskFlow is a full-stack task management web application built with **Python**, **Flask**, **SQLAlchemy**, **SQLite**, **HTML**, **CSS**, and **Jinja2**. It allows users to securely manage their tasks through an intuitive dashboard with authentication, categories, priorities, progress tracking, and profile management.

---

# 🚀 Features

## 👤 User Authentication

- Register a new account
- Secure login
- Logout
- Password hashing with Werkzeug
- Edit profile
- Change password
- Delete account
- Session management
- Protected routes

---

## ✅ Task Management

- Create tasks
- Edit tasks
- Delete tasks
- Mark tasks as completed
- Due dates
- Due date validation
- Priority levels
  - 🔴 High
  - 🟡 Medium
  - 🟢 Low
- Task categories
  - 📚 Study
  - 💼 Work
  - 🏠 Personal
  - ❤️ Health
  - 🛒 Shopping
  - 🎯 Other
- Category editing
- Overdue task highlighting

---

## 📊 Dashboard

- Personalized welcome message
- Total tasks
- Completed tasks
- Pending tasks
- Progress bar
- Completion percentage
- Due today
- Due this week
- High-priority tasks counter
- Category statistics
- Search tasks
- Filter by:
  - Status
  - Priority
  - Category
- Sort tasks by:
  - Newest
  - Oldest
  - Title
  - Due date
- Empty state when no tasks exist

---

## 👤 User Profile

- View profile
- Member since date
- Total tasks
- Completed tasks
- Pending tasks
- Completion percentage
- Edit profile
- Change password

---

## 🛡️ Validation & Security

- Email validation
- Duplicate email prevention
- Strong password requirements
- Password hashing
- Due date validation
- Category validation
- Friendly flash messages
- Login required for protected pages
- Users can only edit or delete their own tasks

---

## 🗄️ Database

- SQLite database
- SQLAlchemy ORM
- Flask-Migrate
- Database migrations
- Persistent user accounts

---

# 🛠️ Technologies Used

## Backend

- Python
- Flask
- SQLAlchemy
- Flask-Migrate
- Werkzeug

## Frontend

- HTML5
- CSS3
- Jinja2

## Database

- SQLite

## Version Control

- Git
- GitHub

---

# 📁 Project Structure

```text
TaskFlow/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── user.py
│   └── task.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   ├── profile.html
│   ├── edit_profile.html
│   ├── edit_task.html
│   ├── login.html
│   ├── register.html
│   ├── 404.html
│   └── 500.html
│
├── static/
│   └── style.css
│
├── migrations/
│
└── instance/
    └── taskflow.db
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/haninatwi0/TaskFlow.git
```

Open the project folder:

```bash
cd TaskFlow
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 📸 Current Features

- ✔ User Authentication
- ✔ Profile Management
- ✔ Change Password
- ✔ Dashboard
- ✔ Task Management
- ✔ Categories
- ✔ Search
- ✔ Filters
- ✔ Sorting
- ✔ Progress Tracking
- ✔ Responsive Design
- ✔ Flask-Migrate Integration

---

# 🚧 Future Improvements

- 📅 Calendar View
- 📊 Charts & Analytics
- 🔔 Notifications & Reminders
- 🌙 Dark Mode
- 📧 Email Verification
- 🔑 Password Reset via Email
- 📄 Export Tasks (CSV / PDF)
- 🖼️ User Avatar
- 🤖 AI Productivity Assistant
- ☁️ PostgreSQL Deployment
- 🚀 Render Production Deployment

---

# 📚 What I Learned

During this project I practiced and improved my knowledge of:

- Flask routing
- SQLAlchemy ORM
- Database migrations with Flask-Migrate
- Authentication and session management
- Password hashing
- CRUD operations
- Form validation
- Jinja templating
- Responsive web design
- Git and GitHub workflow
- Debugging and testing
- Full-stack web application development

---

# 👩‍💻 Author

**Hanin Atwi**

Computer Science Student

This project was built as a portfolio project to strengthen my full-stack web development skills using Flask and modern web technologies.

---

# 📄 License

This project is intended for educational and portfolio purposes.