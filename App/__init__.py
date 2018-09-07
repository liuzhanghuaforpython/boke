from flask import Flask
from flask_bootstrap import Bootstrap
from flask_session import Session

from App.models import db, migrate

from App.views import blue


def create_app():
    app=Flask(__name__)
    app.register_blueprint(blueprint=blue)
    app.config['SECRET_KEY']='120'
    app.config['SESSION_TYPE']='redis'
    Session(app=app)
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123@localhost:3306/liuzhanghua'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.init_app(app=app)
    Bootstrap(app=app)
    migrate.init_app(app=app,db=db)
    return app