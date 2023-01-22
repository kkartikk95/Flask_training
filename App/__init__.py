from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
app = Flask(__name__) #This will make the current file as the main entry point
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

from App import routes
