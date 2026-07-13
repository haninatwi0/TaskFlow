from datetime import datetime
from models.user import db


class Task(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    completed = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    due_date = db.Column(
        db.Date
    )
    
    priority = db.Column(
    db.String(20),
    default="Medium"
    )

    # Connection with User
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )