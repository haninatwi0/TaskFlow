from asyncio import tasks
import email
import re
from flask import Flask, render_template, request, redirect, session, flash 
from werkzeug.security import generate_password_hash, check_password_hash
from models import user
from models.user import db, User
from sqlalchemy.exc import IntegrityError
from models.task import Task

import os
from dotenv import load_dotenv

from datetime import datetime, date



app = Flask(__name__)
load_dotenv()

app.secret_key = os.getenv("SECRET_KEY")

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///taskflow.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Connect database with Flask
db.init_app(app)

print("Database URI:", app.config["SQLALCHEMY_DATABASE_URI"])
print("Current folder:", os.getcwd())


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("Invalid email or password.", "error")
            return redirect("/login")

        if not check_password_hash(user.password, password):
            flash("Invalid email or password.", "error")
            return redirect("/login")

        session["user_id"] = user.id

        flash(f"Welcome back, {user.name}!", "success")

        return redirect("/dashboard")


    return render_template("login.html")

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        flash("Please login first.", "error")
        return redirect("/login")

    user = User.query.get(session["user_id"])

    if not user:
        session.clear()
        flash("Please login again.", "error")
        return redirect("/login")

    search = request.args.get("search", "").strip()
    status = request.args.get("status", "all")
    priority = request.args.get("priority", "all")
    sort = request.args.get("sort", "newest")

    tasks = Task.query.filter_by(user_id=user.id)

    if search:
        tasks = tasks.filter(
            (Task.title.ilike(f"%{search}%")) |
            (Task.description.ilike(f"%{search}%"))
        )

    if status == "completed":
        tasks = tasks.filter_by(completed=True)

    elif status == "pending":
        tasks = tasks.filter_by(completed=False)

    if priority != "all":
        tasks = tasks.filter_by(priority=priority)

    if sort == "newest":
        tasks = tasks.order_by(Task.created_at.desc())

    elif sort == "oldest":
        tasks = tasks.order_by(Task.created_at.asc())

    elif sort == "title":
        tasks = tasks.order_by(Task.title.asc())

    elif sort == "due":
        tasks = tasks.order_by(Task.due_date.asc())

    tasks = tasks.all()
    
    total_tasks = len(tasks)

    completed_tasks = sum(1 for task in tasks if task.completed)

    if total_tasks > 0:
        progress = int((completed_tasks / total_tasks) * 100)
    else:
        progress = 0

    return render_template(
        "dashboard.html",
        user=user,
        tasks=tasks,
        search=search,
        status=status,
        priority=priority,
        sort=sort,
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        progress=progress,
        today=date.today()
    )
    
    
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        if not re.match(email_pattern, email):
            flash("Please enter a valid email address.", "error")
            return redirect("/register")
        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        
        if existing_user:
            flash("Email is already registered.", "error")
            return redirect("/register")

        if len(password) < 8:
            flash("Password must be at least 8 characters long.", "error")
            return redirect("/register")

        if not re.search(r"[A-Z]", password):
            flash("Password must contain an uppercase letter.", "error")
            return redirect("/register")

        if not re.search(r"[a-z]", password):
            flash("Password must contain a lowercase letter.", "error")
            return redirect("/register")

        if not re.search(r"\d", password):
            flash("Password must contain a number.", "error")
            return redirect("/register")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            flash("Password must contain a special character.", "error")
            return redirect("/register")
        password = generate_password_hash(password)
        
        # Create the new user
        new_user = User(
            name=name,
            email=email,
            password=password
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! Please log in.", "success")
        return redirect("/login")
    total_tasks = len(tasks)

    completed_tasks = sum(1 for task in tasks if task.completed)

    if total_tasks > 0:
        progress = int((completed_tasks / total_tasks) * 100)
    else:
        progress = 0
    return render_template("register.html")


@app.route("/add-task", methods=["POST"])
def add_task():

    if "user_id" not in session:
        flash("Please login first.", "error")
        return redirect("/login")


    title = request.form["title"]
    description = request.form["description"]
    due_date = request.form["due_date"]
    user_id = session["user_id"]
    priority = request.form["priority"]

    new_task = Task(

        title=title,

        description=description,

        due_date=datetime.strptime(
            due_date,
            "%Y-%m-%d"
        ).date(),
        
        priority=priority,
        
        user_id=user_id

    )


    db.session.add(new_task)
    db.session.commit()


    return redirect("/dashboard")


@app.route("/complete/<int:id>")
def complete_task(id):
    if "user_id" not in session:
        flash("Please login first.", "error")
        return redirect("/login")
    
    task = Task.query.get(id)

    task.completed = True

    db.session.commit()

    return redirect("/dashboard")


@app.route("/delete/<int:id>")
def delete_task(id):

    if "user_id" not in session:
        flash("Please login first.", "error")
        return redirect("/login")

    task = Task.query.get(id)

    db.session.delete(task)

    db.session.commit()

    return redirect("/dashboard")


@app.route("/logout")
def logout():

    session.clear()

    flash("You have been logged out.", "success")

    return redirect("/login")

@app.route("/delete-account")
def delete_account():

    if "user_id" not in session:
        return redirect("/login")

    user = User.query.get(session["user_id"])

    db.session.delete(user)
    db.session.commit()

    session.clear()

    flash("Your account has been deleted.", "success")

    return redirect("/")



@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):

    if "user_id" not in session:
        return redirect("/login")

    task = Task.query.get_or_404(task_id)

    if task.user_id != session["user_id"]:
        flash("You are not authorized to edit this task.", "error")
        return redirect("/dashboard")

    if request.method == "POST":

        task.title = request.form["title"]
        task.description = request.form["description"]
        task.priority = request.form["priority"]

        due_date = request.form["due_date"]

        if due_date:
            task.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        else:
            task.due_date = None

        db.session.commit()

        flash("Task updated successfully!", "success")

        return redirect("/dashboard")

    return render_template("edit_task.html", task=task)



# Create database tables
with app.app_context():
    db.create_all()


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)