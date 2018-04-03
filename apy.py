#!venv/bin/python

"""
	API Proper
	This top level program handles requests and authetication
	Many database-oriented tasks are offloaded to the db_overlay module
"""

from flask import Flask
import datetime
import random
import config
import users_db_overlay as udb
import posts_db_overlay as pdb

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return "Hello, World!"

@app.route('/signup', methods=['POST'])
def mkuser():
	"""
	Add a new user to the users database
	Inputs:
		JSONified form of a user, takes the form:
			{
				"user": {
					"username": $username
					"realname": $realname
					"password": $password
				}
			}
	"""

	# generate our 32-character long UUUID
	recruit_UUUID=str(abs(int(
		str(hash(datetime.datetime.now))+
		str(random.randint(111111111111,999999999999))
	)))

	if not flask.request.json or not "username" in flask.request.json or not "password" in flask.request.json:
		abort(400)

	# actually add the user
	udb.add_user(
		recruit_UUUID,
		flask.request.json.get("username"),
		flask.request.json.get("realname","anon"),
		flask.request.json.get("password")
	)

@app.route('/howdy')
@app.route('/yeehaw')
def yeehaw():
	return "yeehaw"

@app.route('/hello/<username>')
def sayHi(username):
	return "Hello " + username

@app.errorhandler(404)
def not_found(error):
	return flask.make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	try:
		app.run(
			debug=config.is_debug,
			host=config.system_ip,
			port=config.port
		)
	except:
		try:
			print("Configuration file failed!, falling back to some sane defaults.")
			app.run(
				debug=True,
				host='127.0.0.1'
			)
		except:
			print("Sane defaults failed, you're on your own!")
