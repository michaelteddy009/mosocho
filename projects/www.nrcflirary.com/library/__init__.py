from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import  Bcrypt
#from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f1d7a8e674603540e31e650f3b60313f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
#bcrypt = Bcrypt(app)
#login_manager = LoginManager()

from library import route