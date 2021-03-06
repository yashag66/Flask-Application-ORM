from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')
login = LoginManager(app)
login.login_view = 'login'
login_manager.login_message = "Please login to View the content"
db.init_app(app)


with app.app_context():
    # Imports
    from . import routes

    # Create tables for our models
    db.create_all()

