from flask import Flask

app = Flask(__name__) #This will make the current file as the main entry point

from App import routes
