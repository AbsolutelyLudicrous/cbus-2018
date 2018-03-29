#!venv/bin/python

"""
	Module which abstracts some basic database functions to the APY
	Meant to declutter the APY a little bit
	(Also so that Raghav can do their database wizardry without interference)
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

def get_user(u):
	"""
	Get all attributes of a specified user
	"""
	pass

def set_user(u,new_u):
	"""
	Set the attributes of a specified user
	"""
	pass

def get_user_attr(u,attr):
	"""
	Get a single attribute from a user
	"""
	pass

def set_user_attr(u,attr):
	"""
	Set a single attribute of a user
	"""
	pass
