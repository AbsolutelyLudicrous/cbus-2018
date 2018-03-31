#!venv/bin/python

"""
	Small python script to bootstrap the the databases into a usable state.
	It creates databases coforming the the specs located in data/docs.d
		https://github.com/AbsolutelyLudicrous/cbus-2018/blob/master/data/docs.d/users-db-specification
		https://github.com/AbsolutelyLudicrous/cbus-2018/blob/master/data/docs.d/posts-db-specification

	When imported as a module, it defines some variables representing the database specification

	DO NOT RUN THIS SCRIPT AFTER A DATABASE HAS BEEN BUILT, YOU'LL FUCK UP YOUR EXISTING DATABASE
	ONLY RUN THIS SCRIPT TO BOOTSTRAP THE DATABASE
"""

import sqlite3 as sqlite

users_schema=[
	"UUUID",
	"owned",
	"username",
	"realname",
	"password"
]

if __name__ == "__main__":
	# if we're running the script to bootstrap the database

	# get our cursors and connections ready
	users_conn=sqlite.connect('dbs/users.db')
	posts_conn=sqlite.connect('dbs/posts.db')
	users=users_conn.cursor()
	posts=posts_conn.cursor()

	# turn the schema definition into a sqlized version
	users_sqlized_schema=""
	index=0
	for field in users_schema:
		index+=1
		users_sqlized_schema+=(field+" TEXT")
		users_sqlized_schema+=(",\n\t" if index is not len(users_schema) else "\n\t") # append a comma separator and a newline if this is not the last element in the users schema

	users.execute('''
	CREATE TABLE users (
	'''+users_sqlized_schema+''');
	''')

	users_conn.commit()
	users_conn.close()
