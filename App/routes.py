from App import app
from flask import render_template

@app.route("/") # These are called function decorators
@app.route("/index")
@app.route("/home") # Can stack how many ever routing patterns as we want in the same format
def index():
    return render_template("index.html", login=True)

@app.route("/home") # Can stack how many ever routing patterns as we want in the same format
def index():
    return render_template("index.html", login=True)

@app.route("/home") # Can stack how many ever routing patterns as we want in the same format
def index():
    return render_template("index.html", login=True)

@app.route("/home") # Can stack how many ever routing patterns as we want in the same format
def index():
    return render_template("index.html", login=True)


