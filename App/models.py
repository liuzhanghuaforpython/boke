from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
migrate=Migrate()

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True)
    password=db.Column(db.String(64))
    phone=db.Column(db.String(11))