from App import app
from flask import render_template

@app.route("/") # These are called function decorators
@app.route("/index")
def index():
    return render_template("index.html")