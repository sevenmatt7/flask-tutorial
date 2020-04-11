from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')     #decorators which modifies the function that follows it
@app.route('/index') #when there is a request for the URLs, Flask is going to invoke
                     #and pass the return value back as a response
def index():
	user = {'username': 'Matthew'}
	posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST']) #by default, the method is get
def login():
	form = LoginForm()
	if form.validate_on_submit(): #does the validating of the data
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))

	return render_template('login.html', title='Sign In', form=form)