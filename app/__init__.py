from flask import Flask
from config import Config #config.py is the actual filename while Config is the name of the class
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__) #creates the app object as an instance of class Flask
				      #__name__ is a predefined variable
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

#to workaround circular imports
from app import routes, models  #models has the structure of the database

#routes are the different URLs that the application implements
#handlers for application routes are written as Python functions (view functions)
