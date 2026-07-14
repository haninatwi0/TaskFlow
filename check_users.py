from app import app
from models.user import User

with app.app_context():
    users = User.query.filter_by(email="haninatwi0@gmail.com").all()

    print("Number of accounts:", len(users))

    for user in users:
        print(user.id, user.email, user.name)