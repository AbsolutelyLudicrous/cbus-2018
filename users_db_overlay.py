#!venv/bin/python

"""
	Module which abstracts some basic database functions to the APY
	Meant to declutter the APY a little bit
	(Also so that Raghav can do their database wizardry without interference)

	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	!!                                                                                                                                     !!
	!!  IT IS ASSUMED THAT ALL REQUESTS TO THIS MODULE ARE PRE-AUTHENTICATED BY APY.PY, THIS MODULE DOES NOT DO ANY REQUEST AUTHETICATION  !!
	!!                                                                                                                                     !!
	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

	UNIVERSAL INPUT NOTE:
		All of these functions use either strings or iterables for parameters
		Passing us an integer is just asking for trouble

	Method summaries:
		add_user(string UUUID, opt string username, opt string realname, opt string password)
		get_user(string UUUID)
		set_user(string UUUID, iterable new_user)
			iterable new_user takes form (username,realname,password)
		get_user_attr(string UUUID, string attribute)
		set_user_attr(string UUUID, string attribute, string new_attribute_value)

	Return codes:
		Each method defined here will return either a standard HTTP code as an integer or an iterable containing the requested values
		Setters should always return HTTP codes; specifically 200 OKAY, 400 YOU FUCKED UP; or 500 WE FUCKED UP
		Getters should only return HTTP codes when an error has occured, otherwise they will return the requested data

	Great music to listen to while hacking on this API:
		You Give REST a Bad Name - https://www.youtube.com/watch?v=nSKp2StlS6s
"""

import sqlite3 as sqlite
from db_bootstrap import users_schema

# Connect to out DBs and get the cursors ready
users_conn=sqlite.connect('dbs/users.db')
users=users_conn.cursor()

if __name__ == "__main__":
	print(	"""
		Hey!, uh, you're a little bit supposed to use this as an imported module.
		Like, it's fine if you need to hack something together real quick,
		but this script is really just an abstraction layer over the sqlite3 API.
		Good luck!
		"""
	)

def add_user(uuid,username=None,name=None,pw=None):
	"""
	Add a new user
	Inputs:
		uuid - the UUID of the user to be added
	Optional inputs:
		username - the username to be gotten, defaults to the UUID
		name - the real name of the user
		pw - the password hash of the user
	"""

	# try to insert a column for a new user
	try:
		users.execute('''
			INSERT INTO users (UUUID,username,realname,password)
			VALUES (?,?,?,?);
			''',(uuid,username,name,pw)
		)
	except BaseException as e:
		print(e)
		print("A fatal error occured when creating the user, perhaps the user already exists?")
		return 500	# internal server error

	# save our changes
	users_conn.commit()

	# http 200 okay
	return 200



def get_user(u):
	"""
	Get all attributes of a specified user
	Inputs:
		u - the UUUID of the user to be gotten
	"""

	# try to return the requested user
	try:
		users.execute('''
			SELECT * FROM users WHERE UUUID=?;
			''',(u,)
		)
		retrieved_users = users.fetchall()

		# check that we have found a user with the requested UUUID
		if len(retrieved_users) == 0:
			print("Could not find a user by that UUUID!")
			return 400
		elif len(retrieved_users) > 1:
			print("UwU theh was a fucksy-wucksie! We fwound muwtipuw users wif that UWUID!~~~ xP")	# this is staying in prod until I'm no longer the only person commiting to the repo
			raise Exception("Fucking what!? Multple users found with same UUUID!")
		else:
			return retrieved_users[0]
	except BaseException as e:
		print(e)
		print("A fatal error occured while selecting the requested user")
		return 500



def set_user(u,new_u):
	"""
	Set the attributes of a specified user
	Inputs:
		u - the UUUID of the user to be replaced
		new_u - a complete representation of the new user
			has to be in the form:
			(username,realname,password)
			NOTE that you can not change the UUUID (duh, it's Universally Unique)
	"""

	# try to set the user with the new values
	try:
		users.execute('''
				UPDATE users
				SET	username=?,
					realname=?,
					password=?
				WHERE UUUID=?
			''',((new_u)+(u,))
		)
	except BaseException as e:
		print(e)
		print("A fatal error occured while trying to re-set the user")
		return 500

	# commit our changes
	users_conn.commit()

	# http 200 okay
	return 200



def get_user_attr(u,attr):
	"""
	Get a single attribute from a user
	Inputs:
		u - the UUUID
		attr - the attribute to be gotten
	"""

	# sanity checking
	if attr not in users_schema:
		print("That attribute does not exist!")
		return 400

	# try to return the value corresponding to that attribute
	try:
		return get_user(u)[			# take the list returned by get_user
			users_schema.index(attr)	# and get its position in the list returned by get_user
		]
	except BaseException as e:
		print(e)
		print("A fatal error occured while trying to fetch that attribute")
		return 500



def set_user_attr(u,attr,val):
	"""
	Set a single attribute of a user
	Inputs:
		u - the UUUID of the user to be operated on
		attr - the attribute to be set
			can be either username, realname, or password
		val - the value the attribute will be set to
	"""

	# sanity check the attribute we were asked to set
	if attr not in users_schema:
		print("That attribute does not exist!")
		return 400

	# try to set the value
	try:
		users.execute('''
				UPDATE users
				SET '''+attr+'''=?
				WHERE UUUID=?;
			''',(val,u)
			#| doing string catenation in SQL would normally be insecure,
			#| but we validate the attribute requested againt a list of valid attributes so it's hopefully fine
			#| (also this is literally the only way to have a variable field be substituted, otherwise we get a syntax error)
		)
	except BaseException as e:
		print(e)
		print("A fatal error occured while trying to set the value")
		return 500

	# save our changes
	users_conn.commit()

	# http 200 okay
	return 200
