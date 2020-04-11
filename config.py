import os 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	#The idea is that a value sourced from an environment variable is preferred,
    #but if the environment does not define the variable, 
    #then the hardcoded string is used instead. 
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'whatisup'

	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
		'sqlite:///' + os.path.join(basedir, 'app.db')
	#set to false because this will signal the application everytime a change is about 
	#to be made
	SQLALCHEMY_TRACK_MODIFICATIONS = False