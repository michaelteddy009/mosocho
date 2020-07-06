from flask import Flask, render_template, url_for, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)  #enables flask know where to start looking in thee code
app.config['SECRET_KEY'] = '7a24f70481f92038d2bf0371332a71a7'

posts = [
	{
	'title':'Blog post 1',
	'author':'Michael Ochara',
	'content':'content of blog post 1'
	},
	{
	'title':'Blog post 2',
	'author':'Joel Osteen',
	'content':'content of blog post 2'
	}
]

@app.route('/')
def index():
	return render_template('index.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username}!', 'success')
		return redirect(url_for('/'))
	return render_template('register.html', title='register', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='register', form=form)


if __name__ == "__main__":
	app.run(debug=True)


'''To run the code we first run export/set FLASK_APP ==index.py then flask run we also set the FLASK_DEBUG=1 in the command line'''
