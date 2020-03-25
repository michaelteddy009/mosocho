from flask import render_template, url_for, flash, redirect
from library import app, db 
from library.forms import RegistrationForm, LoginForm
from library.models import User
#from flask_login import login_user

@app.route('/home')
def home():
	return render_template('home.html', title='home')

@app.route('/about')
def about():
	return render_template('about.html', title='about')

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		#user = User.query.filter_by(email=form.email.data).first()
		if form.email.data =='lib@gmail.com' and form.password.data=='lib':
			#login_user(user, rember=form.remember.data)
			flash(f'Logged In as {form.email.data}')
			return redirect(url_for('about'))
		else:
			flash("Login unsuccessful. Please Check Email and Password")
	return render_template('login.html', title='login', form=form) 

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():

		#hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=form.password.data)
		db.session.add(user)
		db.session.commit()


		flash(f"{form.username.data} Your Account Has Now Been Created, You Can Now Log In")
		return redirect(url_for('login'))
	return render_template('register.html', title='register', form=form)




'''@app.route('')
def ():
	return '''