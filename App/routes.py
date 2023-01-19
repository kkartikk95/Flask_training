from App import app
from flask import render_template

@app.route("/") # These are called function decorators
@app.route("/index")
@app.route("/home") # Can stack how many ever routing patterns as we want in the same format
def index():
    return render_template("index.html", index=True)

@app.route("/login") # Can stack how many ever routing patterns as we want in the same format
def login():
    return render_template("login.html", login=True)

@app.route("/courses") # Can stack how many ever routing patterns as we want in the same format
@app.route("/courses/<term>")
def courses(term = "Spring 2019"):
    courseData = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP",
                   "credits":3,"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1",
                    "description":"Intro to Java Programming","credits":4,"term":"Spring"},
                  {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming",
                   "credits":3,"term":"Fall"}, {"courseID":"4444","title":"Angular 1",
                    "description":"Intro to Angular","credits":3,"term":"Fall, Spring"},
                  {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming",
                   "credits":4,"term":"Fall"}]

    return render_template("courses.html", courseData=courseData, courses=True, term=term)

@app.route("/register") # Can stack how many ever routing patterns as we want in the same format
def register():
    return render_template("register.html", register=True)


