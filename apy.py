#!venv/bin/python

"""
	API Proper
	This top level program handles requests and authetication
	Many database-oriented tasks are offloaded to the db_overlay module
"""

from flask import Flask
import datetime
import random
import socket
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
	"""

	# generate our 32-character long UUUID
	recruit_UUUID=str(abs(int(
		str(hash(datetime.datetime.now))+
		str(random.randint(111111111111,999999999999))
	)))

if __name__ == '__main__':
	app.run(
		debug=True, 
		host=socket.gethostbyname('cutie-computie.org'),
		port=808
	)
