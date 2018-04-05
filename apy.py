#!venv/bin/python

"""
	API Proper
	This top level program handles requests and authetication
	Many database-oriented tasks are offloaded to the db_overlay module
"""

from flask import Flask
from flask import request
import datetime
import random
import sys
import users_db_overlay as udb
import posts_db_overlay as pdb

app = Flask(__name__)



@app.route('/add-post', methods=['POST'])
def add_post():
	try:
		post_username=request.get_json()["username"]
		post_password = request.get_json()["password"]
		post_title = request.get_json()["title"]
		post_contents = request.get_json()["contents"]
		post_tags = request.get_json()["tags"]
	except BaseException as e:
		print(e)
		return 400

	
	post_UUUID = udb.get_user_by_username(post_username)
	if (post_UUUID == 400):
		return 400


	actual_password = udb.get_user_attr(post_UUUID, "password")
	if (actual_password == post_password):
		#access granted
				
		recruit_PUUID=	str(abs(hash(str(abs(int(str(hash(datetime.datetime.now))+str(random.randint(1, 9999999999999999))))))))
		pdb.add_post(recruit_PUUID, post_title, post_username, post_contents, post_tags)

			
		


@app.route('/', methods=['GET'])
def index():
	return """
	Hey howdy hey!
	Congratulations, your connection to the server worked!
	(Now go read the API docs to figure out how to do useful things with the API.)
	"""


@app.route('/howdy', methods=['GET'])
@app.route('/yeehaw', methods=['GET'])
def yeehaw():
	return "Yeehaw!"



@app.route('/hello/<username>', methods=['GET'])
def sayHi(username):
	return "Hello " + username



@app.route('/echo', methods=['POST'])
def echo():
	"""
	Echo all data thrown at us back at the CURLer
	"""
	return request.data



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

	# W H I T E S P A C E M A K E S Y O U R C O D E M O R E R E A D A B L E

	# generate our UUUID
	recruit_UUUID=	str(
				abs(
					hash(
						str(
							abs(
								int(
									str(
										hash(
											datetime.
												datetime.
													now
										)
									)
									+
									str(
										random.
											randint(
												1,
												9999999999999999
											)
									)	# using randint isn't cryptographically secure, but we don't need crypto-level security for the UUUID
								)
							)
						)
					)
				)
			)

	# try to pull user information out of received json, may fail if the JSONified user representation was incomplete
	try:
		# pull other information out of the JSON we got
		recruit_username=request.get_json()["username"]
		recruit_realname=request.get_json()["realname"]
		recruit_password=request.get_json()["password"]
	except BaseException as e:
		print(e)
		return 400

	try:
		if udb.get_user_by_username(recruit_username) is not []:
			# add the user
			udb.add_user(recruit_UUUID, recruit_username, recruit_realname, recruit_password)
	except BaseException as e:
		print(e)
		return """
		Either somebody has already taken that username in the database or that is an invalid username.
		""",405

	return str(udb.get_user(recruit_UUUID)),200



if __name__ == '__main__':
	if "home" in sys.argv:
		"""
		Two scenarios:
			- we're running on prod, in which case assigning an IP and port and stuff works fine
			- we're running on dev (read: our own personal computers), in which case we want to use localhost:5000 anyways
		The script defaults to running as if on prod, but supplying "home" as an argument will run the API on localhost:5000
		"""

		# run apy.py on localhost:5000
		app.run(
			debug=True,
			host='127.0.0.1'
		)
	else:
		# (try) to run according to the config file
		try:
			# try to load the config file, located in /config.py
			import config
			app.run(
				debug=config.is_debug,
				host=config.system_ip,
				port=config.port
			)
		except BaseException as e:
			try:
				print(e)
				print("Configuration file failed!, falling back to some sane defaults.")
				app.run(
					debug=True,
					host='127.0.0.1'
				)
			except:
				# SHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITSHITS
				print("Sane defaults failed, you're on your own!")
				print("(Good luck!)")
