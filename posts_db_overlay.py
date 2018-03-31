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

	Return codes:
		Each method defined here will return either a standard HTTP code as an integer or an iterable containing the requested values
		Setters should always return HTTP codes; specifically 200 OKAY, 400 YOU FUCKED UP; or 500 WE FUCKED UP
		Getters should only return HTTP codes when an error has occured, otherwise they will return the requested data

	Great music to listen to while hacking on this API:
		You Give REST a Bad Name - https://www.youtube.com/watch?v=nSKp2StlS6s
"""

import sqlite3 as sqlite
from db_bootstrap import posts_schema

# Connect to our DBs and get the cursors ready
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

def add_post(p,title=None,owner=None,contents=None,tags=None):
	"""
	Add an event posting to the database
	Inputs:
		p - the PUUID of the posting
	Optional inputs:
		title - the title of the post
		owner - the !!USERNAME!! of the user who owns the post (see data/docs.d/posts-db-specification for rationale)
		contents - a dict representing all known information about the event
		tags - a string of comma-separated tags associated with the event
	"""

	# try to add a new column
	try:
		posts.execute('''
			INSERT INTO posts (PUUID, title, owner, contents, tags)
			VALUES (?,?,?,?,?);
			''',(p,title,owner,contents,tags)
		)
	except BaseException as e:
		print(e)
		print("A fatal error occurred while adding a new column to the event postings database")
		return 500
	
	# save our changes
	posts_conn.commit()

	# http 200 okay
	return 200
