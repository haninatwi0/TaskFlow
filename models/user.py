from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(200),
        nullable=False
    )
    
    joined_at = db.Column(
    db.DateTime,
    default=datetime.utcnow
    )
    
    tasks = db.relationship(
        "Task",
        backref="owner",
        lazy=True
    )

    def __repr__(self):
        return f"<User {self.email}>"