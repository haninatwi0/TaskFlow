from flask import Flask, render_template, request, redirect, session, flash 
from werkzeug.security import generate_password_hash, check_password_hash
from models import user
from models.user import db, User
from sqlalchemy.exc import IntegrityError
from models.task import Task

import os
from dotenv import load_dotenv

from datetime import datetime

app = Flask(__name__)
load_dotenv()

app.secret_key = os.getenv("SECRET_KEY")

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///taskflow.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Connect database with Flask
db.init_app(app)


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

    return render_template(
        "dashboard.html",
        user=user,
        tasks=user.tasks
    )
    
    
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email is already registered.", "error")
            return redirect("/register")

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