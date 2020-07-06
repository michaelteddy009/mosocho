from flask import render_template, url_for, flash, redirect
from library import app, db, bcrypt
from library.forms import RegistrationForm, LoginForm
from library.models import User
from flask_login import login_user, current_user

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
		user =  User.query.filter_by(email=form.email.data).first()
		if user.password == form.password.data:
		#if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user) #", rember=form.remember.data" should be added as an aurgument
			flash(f'Logged In as email')
			return redirect(url_for('about'))
		else:
			flash(f"Login unsuccessful. Please Check Email and Password")
	else:
		flash(f"Was not succeful on submission validation")
		return render_template('login.html', title='login', form=form)
	return render_template('login.html', title='login', form=form) 

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f"{form.username.data} Your Account Has Now Been Created, You Can Now Log In")
		return redirect(url_for('login'))
	return render_template('register.html', title='register', form=form)




'''@app.route('')
def ():
	return '''