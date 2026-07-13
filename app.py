from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import db, User
from sqlalchemy.exc import IntegrityError
from models.task import Task

app = Flask(__name__)
app.secret_key = "your-secret-key"

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

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            return redirect("/dashboard")

        return "Invalid email or password!"

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    user = User.query.get(session["user_id"])

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

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return "Email already registered!"

        new_user = User(
            name=name,
            email=email,
            password=password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")

@app.route("/add-task", methods=["POST"])
def add_task():

    if "user_id" not in session:
        return redirect("/login")


    title = request.form["title"]
    description = request.form["description"]


    task = Task(
        title=title,
        description=description,
        user_id=session["user_id"]
    )


    db.session.add(task)
    db.session.commit()


    return redirect("/dashboard")


@app.route("/complete/<int:id>")
def complete_task(id):

    task = Task.query.get(id)

    task.completed = True

    db.session.commit()

    return redirect("/dashboard")


@app.route("/delete/<int:id>")
def delete_task(id):

    task = Task.query.get(id)

    db.session.delete(task)

    db.session.commit()

    return redirect("/dashboard")


@app.route("/logout")
def logout():

    session.pop("user_id", None)

    return redirect("/login")

# Create database tables
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)