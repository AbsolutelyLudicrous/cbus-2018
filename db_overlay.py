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
"""

import sqlite3 as sqlite

posts=sqlite.connect('dbs/posts.db')
users=sqlite.connect('dbs/users.db')

if __name__ == "__main__":
	print(	"""
		Hey!, uh, you're a little bit supposed to use this as an imported module.
		Like, it's fine if you need to hack something together real quick,
		but this script is really just an abstraction layer over the sqlite3 API.
		Good luck!
		"""
	)

def add_user(uuid,username=uuid,name=None,pw=None,prefs=None):
	"""
	Add a new user
	Inputs:
		uuid - the UUID of the user to be added
	Optional inputs:
		username - the username to be gotten, defaults to the UUID
		name - the real name of the user
		pw - the password hash of the user
		prefs - the users preferences
	"""
	users.execute('''
		CREATE TABLE ? (
			username TEXT,
			realname TEXT,
			password TEXT,
			preferences TEXT
		);''',uuid)
	users.execute('''
		INSERT INTO ? (username,realname,password,preferences)
		VALUES (?,?,?,?);''',(uuid,username,name,pw,prefs))

def get_user(u):
	"""
	Get all attributes of a specified user
	Inputs:
		u - the user to be gotten
	"""
	pass

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
