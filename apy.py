#!venv/bin/python

"""
	API Proper
	This top level program handles requests and authetication
	Many database-oriented tasks are offloaded to the db_overlay module
"""

from flask import Flask
import users_db_overlay as udb

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/yeehaw')
def yeehaw():
	return "yeehaw"

@app.route('/hello/<username>')
def sayHi(username):
	return "Hello " + username


if __name__ == '__main__':
    app.run(debug=True)
