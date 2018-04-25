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
import random
import sqlite3 as sqlite
from db_bootstrap import posts_schema

# Connect to our DBs and get the cursors ready
posts_conn=sqlite.connect('dbs/posts.db', check_same_thread=False)
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
			INSERT INTO posts (PUUID, title, owner, contents, comments, RSVPers, tags)
			VALUES (?,?,?,?,?,?,?);
			''',(p,title,owner,contents,"","",tags)
		)
	except BaseException as e:
		print(e)
		print("A fatal error occurred while adding a new column to the event postings database")
		return 500

	# save our changes
	posts_conn.commit()

	# http 200 okay
	return 200



def get_post(p):
	"""
	Get a post by PUUID
	Inputs:
		p - the PUUID
	"""

	try:
		posts.execute('''
			SELECT * FROM posts
			WHERE PUUID=?;
			''',(p,)
		)
		retrieved_posts=posts.fetchall()

		if len(retrieved_posts) == 0:
			print("Could not find any post by that PUUID")
			return 400
		elif len(retrieved_posts) > 1:
			print("Found multiple posts by that PUUID!?!?")
			raise Exception("What the fuck?! Found multiple event postings with that PUUID?! This shouldn't happen!")
		else:
			return retrieved_posts[0]
	except BaseException as e:
		print(e)
		print("A fatal error occured while trying to retrive that post")
		return 500


"""
def set_post(p,new_p):
	Set every attribute of an event posting
	Inputs:
		p - the PUUID of the post to be set
		new_p - the complete representation of the new post
			takes the form: (title, owner, contents, tags)

	# try to completely set the post
	try:
		posts.execute('''
				UPDATE posts
				SET	title=?,
					owner=?,
					contents=?,
					tags=?
				WHERE PUUID=?;
			''',((new_p)+(p,))
		)
		return 200
	except BaseException as e:
		print(e)
		print("A fatal error occurred while trying to re-set that post!")
		return 500



"""

def get_post_attr(p,attr):
	"""
	Get a single attribute from a user
	Inputs:
		p - the PUUUID
		attr - the attribute to be gotten
	"""

	# sanity checking
	if attr not in posts_schema:
		print("That attribute does not exist!")
		return 400

	# try to return the value corresponding to that attribute
	try:
		return get_post(u)[			# take the list returned by get_user
			posts_schema.index(attr)	# and get its position in the list returned by get_user
		]
	except BaseException as e:
		print(e)
		print("A fatal error occured while trying to fetch that attribute")
		return 500





def set_post_attr(p,attr,val):
	"""
	Set a single attribute of a user
	Inputs:
		p - the PUUUID of the user to be operated on
		attr - the attribute to be set
			can be used to set anything, primarily will be used to update the contents, RSVPers and comments fields
		val - the value the attribute will be set to
	"""

	# sanity check the attribute we were asked to set
	if attr not in posts_schema:
		print("That attribute does not exist!")
		return 400

	# try to set the value
	try:
		posts.execute('''
				UPDATE posts
				SET '''+attr+'''=?
				WHERE PUUUID=?;
			''',(val,p)
			#| doing string catenation in SQL would normally be insecure,
			#| but we validate the attribute requested againt a list of valid attributes so it's hopefully fine
			#| (also this is literally the only way to have a variable field be substituted, otherwise we get a syntax error)
		)
	except BaseException as e:
		print(e)
		print("A fatal error occured while trying to set the value")
		return 500

	# save our changes
	posts_conn.commit()

	# http 200 okay
	return 200


def get_events_by_tag(tags):
	list_tags = []
	while (len(tags) > 0):
		if ',' in tags:		
			commaIndex = tags.index(',')
			
			list_tags.append(tags[0:commaIndex])
			tags = tags[2:]
		else:
			#tags is empty
			list_events.append(tags)			
			tags = ""
	
	list_events = []

	for i in range(0, len(list_tags)):
		posts.execute('''
			SELECT * FROM posts
			WHERE tags LIKE '*?*';
			''',(list_tags[i],)
		)
	
		retrieved_posts=posts.fetchall()
		list_events.append(retrieved_posts)
		print(retrieved_posts)

	return_list = []
	for i in range(0, 50):
		the_event = random.choice(random.choice(list_events))
		return_list.append(the_event)

	while i < (len(return_list) - 1):
		j = i+1
		while j < len(return_list):
			if (return_list[i][posts_schema.index("PUUID")] == return_list[j][posts_schema.index("PUUID")]):
				return_list.pop(j)
			j += 1
		i += 1

	return return_list







