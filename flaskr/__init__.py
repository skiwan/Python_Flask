import os
from flask import Flask

# Application factory function
def create_app(test_config=None):
	#create and configure the app
	app = Flask(__name__,instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path,'flaskr.sqlite'),
		)

	if test_config is None:
		#load the isntance config, if it exists, when not load testing
		app.config.from_pyfile('config.py',silent=True)
	else:
		# load the test config is passed in as parameter
		app.config.from_mapping(test_config)

	# ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass
	""" Only imported when function called """
	from . import db
	db.init_app(app)

	""" REGISTER BLUEPRINTS """		

	from . import auth
	app.register_blueprint(auth.bp)

	# a simple page that says hello
	@app.route('/hello')
	def hello():
		return '#Hello, Rafi!'

	return app