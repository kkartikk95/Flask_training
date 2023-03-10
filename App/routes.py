from App import app, db
from flask import render_template, request, json, Response, redirect, flash
from App.models import User,Course,Enrollment
from App.forms import LoginForm,RegistrationForm


courseData = [{"courseID": "1111", "title": "PHP 101", "description": "Intro to PHP",
               "credits": 3, "term": "Fall, Spring"},
              {"courseID": "2222", "title": "Java 1",
                "description": "Intro to Java Programming", "credits": 4,
                "term": "Spring"},
              {"courseID": "3333", "title": "Adv PHP 201", "description": "Advanced PHP Programming",
               "credits": 3, "term": "Fall"},
              {"courseID": "4444", "title": "Angular 1",
                "description": "Intro to Angular", "credits": 3, "term": "Fall, Spring"},
              {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming",
               "credits": 4, "term": "Fall"}]

@app.route("/") # These are called function decorators
@app.route("/index")
@app.route("/home") # Can stack how many ever routing patterns as we want in the same format
def index():
    return render_template("index.html", index=True)

@app.route("/login", methods=['GET','POST']) # Can stack how many ever routing patterns as we want in the same format
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if request.form.get("email") == "test@uta.com":
            flash("You are Successfully Logged in!","success")
            return redirect("/index")
        else:
            flash("Please recheck credentials","danger")
    return render_template("login.html", form=form, title="Login", login=True)

@app.route("/courses") # Can stack how many ever routing patterns as we want in the same format
@app.route("/courses/<term>")# sending the term as a variable to the courses.html
def courses(term = "Spring 2019"):

    return render_template("courses.html", courseData=courseData, courses=True, term=term)

@app.route("/register")
def register():
    return render_template("register.html", register=True)

@app.route("/enrollment", methods=["GET","POST"])
def enrollment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template("enrollment.html", enrollment=True, data={"id":id,"title":title,"term":term})

@app.route("/api")
@app.route("/api/<idx>")
def api(idx=None):
    if idx == None:
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    return Response(json.dumps(jdata), mimetype="application/json")

@app.route("/user")
def user():
    User(user_id=1, first_name="kartik", last_name="venkat", email="kartik@uta.com",
        password="abc1234").save()
    User(user_id=2, first_name="saw", last_name="see", email="seesaw@uta.com",
         password="1234abc").save()
    users = User.objects.all()
    return render_template("user.html", users=users)