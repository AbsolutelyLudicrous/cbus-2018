#!venv/bin/python3

"""
	Add some test things to the databases
"""

import users_db_overlay as udb
import posts_db_overlay as pdb
import datetime
import random

for i in range(0,30):
	udb.add_user(
		(str(
			str(abs(hash(str(datetime.datetime.now())))) +
			str(abs(hash(str(random.randint(0,12345678910111213141516171819)))))
		)),	#"good enough" UUUID generation
		(chr(random.randint(62,122))),	#random name makin'
		(chr(random.randint(62,122))),	#random name makin'
		(hash(chr(random.randint(62,122))))	#passwordin'
	)

for i in range(0,30):
	pdb.add_post(
		(str(
			str(abs(hash(str(datetime.datetime.now())))) +
			str(abs(hash(str(random.randint(0,12345678910111213141516171819)))))
		)),	#"good enough" PUUID generation
		(chr(random.randint(62,122))),	#title
		(chr(random.randint(62,122))),	#owner
		(str(
			{
				random.randint(0,32):chr(random.randint(62,122)),
				random.randint(0,32):chr(random.randint(62,122)),
				random.randint(0,32):chr(random.randint(62,122)),
				random.randint(0,32):chr(random.randint(62,122)),
				random.randint(0,32):chr(random.randint(62,122))
			}
		)),	#contents
		str(
                    (chr(random.randint(62,122)))+"stuff"
                )
	)
