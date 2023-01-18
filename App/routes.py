from App import app
from flask import render_template

@app.route("/") # These are called function decorators
@app.route("/index")
@app.route("/home") # Can stack how many ever routing patterns as we want in the same format
def index():
    return render_template("index.html", login=True)

@app.route("/login") # Can stack how many ever routing patterns as we want in the same format
def login():
    return render_template("login.html", login=True)

@app.route("/courses") # Can stack how many ever routing patterns as we want in the same format
def courses():
    return render_template("course.html", login=True)

@app.route("/register") # Can stack how many ever routing patterns as we want in the same format
def register():
    return render_template("register.html", login=True)


