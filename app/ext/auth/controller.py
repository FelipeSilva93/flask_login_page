from app.ext.db import db
from app.ext.db.models import User


def create_user(email, password):
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return user


def check_user_existance(email):
    user = db.session.query(User).filter(User.email == email).one()

    return user
