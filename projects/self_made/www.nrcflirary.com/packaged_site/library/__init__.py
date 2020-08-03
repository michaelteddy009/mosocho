from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import werkzeug.security as security
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f1d7a8e674603540e31e650f3b60313f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from library import route