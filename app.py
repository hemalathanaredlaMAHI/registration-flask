from flask import Flask, render_template, request
app=Flask(__name__)

# creating main route, with name and dynamic name paths 

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
        return render_template("details.html", f_name=f_name, l_name=l_name,email=email)

