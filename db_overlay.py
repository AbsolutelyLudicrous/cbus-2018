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
		return users.execute('''
			SELECT * FROM users WHERE UUUID="?";
			''',(u,)
		)
	except BaseException as e:
		print(e)
		print("A fatal error occured while selecting the requested user")
		return 500



def set_user(u,new_u):
	"""
	Set the attributes of a specified user
	Inputs:
		u - the user to be replaced
		new_u - a complete representation of the new user
	"""
	pass



def get_user_attr(u,attr):
	"""
	Get a single attribute from a user
	Inputs:
		u - the user
		attr - the attribute to be gotten
	"""
	pass



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
