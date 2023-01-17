from App import app

@app.route("/") # These are called function decorators
@app.route("/index")
def index():
    return "<h2>Hello Flask</h2>"