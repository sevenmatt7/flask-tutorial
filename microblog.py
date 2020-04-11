from app import app, db #the flask application is app, a member of the app package
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Post': Post}