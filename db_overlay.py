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

	Great music to listen to while hacking on this API:
		- https://www.youtube.com/watch?v=nSKp2StlS6s
"""

import sqlite3 as sqlite

# Connect to out DBs and get the cursors ready
users_conn=sqlite.connect('dbs/users.db')
users=users_conn.cursor()
posts_conn=sqlite.connect('dbs/posts.db')
posts=posts_conn.cursor()

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
		found_user = users.fetchall()[0]	# the "[0]" on the end is needed because .fetchall returns a list of all matching columns

		# check that we have found a user with the requested UUUID
		if found_user != []:
			return found_user
		else:
			return 404

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
	pass



def get_user_attr(u,attr):
	"""
	Get a single attribute from a user
	Inputs:
		u - the UUUID
		attr - the attribute to be gotten
	"""

	# define a dict containing the valid attributes we can access and their positions in the tuple returned by get_user
	attrs={
		"UUUID":0,
		"username":1,
		"realname":2,
		"password":3	# AGAIN!, we do NOT do authentication in this module, do that in apy.py
	}

	if attr not in attrs:
		print("That attribute does not exist!")
		return 400

	# try to return the value corresponding to that attribute
	try:
		return get_user(u)[	# take the list returned by get_user
			attrs[attr]	# ...and use the attrs dict to map the requested attribute to a numerical index
		]
	except BaseException as e:
		print(e)
		print("A fatal error occured while trying to fetch that attribute")
		return 500



def set_user_attr(u,attr):
	"""
	Set a single attribute of a user
	Inputs:
		u - the user
		attr - the attribute to be set
	"""
	pass



def get_post(p):
	"""
	Get the representation of a single post
	Inputs:
		p - the ID post to be gotten
	"""
	pass
