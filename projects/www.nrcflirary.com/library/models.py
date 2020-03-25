from library import db
from datetime import datetime


#video part 6 minute 24 explains the use of sessions

'''@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))'''

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(60), nullable=False, default='default.jpg')
	password = db.Column(db.String(30), nullable=False)

	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.image_file}','{self.password}')"

class Borrow(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime(60), nullable=False, default=datetime.utcnow)

	#video 4 minute 17:30 to explains the making of databases

	def __repr__(self):
		return f"Borrow('{self.title}','{self.DatePosted}')"
