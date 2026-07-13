# TaskFlow 🚀

A modern task management web application built with **Flask**, designed to help users organize, track, and manage their daily tasks efficiently.

TaskFlow provides a complete full-stack experience with user authentication, database management, and CRUD operations. The project was developed to practice backend development, database integration, and building a structured web application using Python.

---

## 📌 Features

### 🔐 User Authentication

* User registration system
* Secure password hashing
* Login and logout functionality
* Session-based authentication
* Protection of private pages

### ✅ Task Management

* Create new tasks
* View personal tasks
* Mark tasks as completed
* Delete tasks
* Tasks are linked to individual user accounts

### 🎨 User Interface

* Custom dark theme design
* Black and pink visual identity
* Responsive page structure
* Shared layout using Flask templates

### 🗄️ Database

* SQLite database integration
* SQLAlchemy ORM
* User and Task data models
* Relationship between users and their tasks

---

## 🛠️ Technologies Used

### Backend

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* Werkzeug Security

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Development Tools

* Git & GitHub
* Virtual Environment (`venv`)
* Python-dotenv

---

## 📂 Project Structure

```
TaskFlow/

│
├── app.py                 # Main Flask application
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
├── .env                   # Environment variables
├── taskflow.db            # SQLite database
│
├── models/
│   ├── user.py            # User database model
│   └── task.py            # Task database model
│
├── templates/
│   ├── base.html          # Main layout
│   ├── index.html         # Home page
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   └── dashboard.html     # User dashboard
│
└── static/
    └── css/
        └── style.css      # Application styling
```

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_LINK
```

### 2. Navigate to the project folder

```bash
cd TaskFlow
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create environment variables

Create a file named:

```
.env
```

Add:

```
SECRET_KEY=your_secret_key
```

### 7. Run the application

```bash
python app.py
```

The application will be available at:

```
http://127.0.0.1:5000
```

---

## 🧠 What I Learned

Through this project, I practiced:

* Building a complete Flask application
* Creating backend routes and handling requests
* Working with databases using ORM
* Designing relational database models
* Implementing authentication systems
* Managing user sessions
* Structuring a professional GitHub repository

---

## 🚀 Future Improvements

Planned features:

* [ ] Task categories
* [ ] Due dates and reminders
* [ ] Task priority levels
* [ ] Search and filtering
* [ ] User profile customization
* [ ] REST API integration
* [ ] Deployment with cloud hosting
* [ ] React frontend version

---

## 👩‍💻 Author

**Hanin Atwi**

Computer Science Student

Interested in software development, backend engineering, and building practical applications.

---

## 📄 License

This project is created for educational and portfolio purposes.