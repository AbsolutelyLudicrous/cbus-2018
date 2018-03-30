#!venv/bin/python

"""
	Small python script to bootstrap the the databases into a usable state.
	It creates databases coforming the the specs located in data/docs.d
		https://github.com/AbsolutelyLudicrous/cbus-2018/blob/master/data/docs.d/users-db-specification
		https://github.com/AbsolutelyLudicrous/cbus-2018/blob/master/data/docs.d/posts-db-specification

	DO NOT RUN THIS SCRIPT AFTER A DATABASE HAS BEEN BUILT, YOU'LL FUCK UP YOUR EXISTING DATABASE
	ONLY RUN THIS SCRIPT TO BOOTSTRAP THE DATABASE
"""

import sqlite3 as sqlite

users=sqlite.connect('dbs/users.db').cursor()
posts=sqlite.connect('dbs/posts.db').cursor()

users.execute('''
	CREATE TABLE users (
		UUUID TEXT,
		username TEXT,
		realname TEXT,
		password TEXT
	);
''')
