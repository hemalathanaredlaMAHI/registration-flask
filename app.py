from flask import Flask, render_template, request
from models import *
from datetime import datetime
import os

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
# creating main route, with name and dynamic name paths 

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template("register.html")

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        f_name=request.form.get('first_name')
        l_name=request.form.get('last_name')
        email=request.form.get('email')
        password=request.form.get('password')
        time1=datetime.now()
        print(time1)
        r=Register(fname=f_name,lname=l_name,email=email,password=password)
        db.session.add(r)
        # db.session.delete()
        db.session.commit()

        s=Register.query.all()
        # db.session.delete(s)
        # db.session.commit()
        # for i in s:
        #     print(f"{i.time}")
        
        return render_template("sample3.html",s=s)


    # if request.method=="GET":
    #     return render_template("register.html")
    # else:
    #     f_name=request.form.get('first_name')
    #     l_name=request.form.get('last_name')
    #     email=request.form.get('email')
    #     return render_template("details.html", f_name=f_name, l_name=l_name,email=email)

