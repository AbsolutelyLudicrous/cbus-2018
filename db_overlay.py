#!venv/bin/python

"""
	Module which abstracts some basic database functions to the APY
	Meant to declutter the APY a little bit
	(Also so that Raghav can do their database wizardry without interference)
"""

import sqlite3 as sqlite

posts=sqlite.connect('posts.db')
users=sqlite.connect('users.db')
