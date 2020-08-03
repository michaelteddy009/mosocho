from flask import render_template, url_for, flash, redirect
from library import app, db, security
from library.forms import RegistrationForm, LoginForm
from library.models import User
from flask_login import login_user, current_user, login_required

@app.route('/home')
def home():
	return render_template('home.html', title='home')



@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if security.check_password_hash(user.password, form.password.data):
				login_user(user, form.remember.data)
				flash(f'Logged in as {user.email}')
				return redirect(url_for('about'))
		return flash(f'This aint working')

	return render_template('login.html', title='login', form=form) 



@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = security.generate_password_hash(form.password.data)
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f"{form.username.data} Your Account Has Now Been Created, You Can Now Log In")
		return redirect(url_for('login'))
	return render_template('register.html', title='register', form=form)


@app.route('/about')
@login_required
def about():
	return render_template('about.html', title='about')

'''@app.route('')
def ():
	return '''