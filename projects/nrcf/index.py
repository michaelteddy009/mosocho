from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/home')
def home():
	return render_template('home.html', title='home')

@app.route('/about')
def about():
	return render_template('about.html', title='about')

@app.route('/login')
def login():
	return render_template('login.html', title='login') 

@app.route('/register')
def register():
	return render_template('register.html', title='register')




'''@app.route('')
def ():
	return '''




if __name__ == '__main__':
	app.run(debug=True)