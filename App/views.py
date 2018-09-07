import hashlib

from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify

from App.models import User, db

blue=Blueprint("first",__name__)
@blue.route('/')
def hello_world():
    return 'Hello World!'

@blue.route('/index/')
def index():
    return render_template("index.html")

@blue.route('/register/',methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    if request.method=="POST":
        name=request.form.get("uname")
        password=request.form.get("upwd")
        phone=request.form.get("phone")
        user=User()
        user.name=name
        user.password=getMd5(password)
        user.phone=phone
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('first.login'))

def getMd5(password):
    MD5=hashlib.md5()
    MD5.update(password.encode('utf-8'))
    return MD5.hexdigest()

@blue.route('/login/',methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template('login.html')
    if request.method=="POST":
        uname=request.form.get("uname")
        upassword=request.form.get("upwd")
        user=User.query.filter_by(name=uname).first()
        if user:
            if user.password==getMd5(upassword):
                session['user_id']=user.id
                return render_template('index.html',user=user)

        return render_template('login.html')

@blue.route('/checkUser/')
def checkUser():
    uname=request.args.get("uname")
    user=User.query.filter_by(name=uname).first()
    data={}
    if user:
        data["code"]=901
    else:
        data["code"]=200
    return jsonify(data)

@blue.route('/loginOut/')
def loginOut():
    session.pop('user_id',None)
    return redirect('/index/')
