#!/usr/bin/env sh

# simple script to setup a new virtualenv to run this server
# invoke it from the project root directory, as such:
# 	sh data/technical.d/setup-venv.sh

# error codes:
# 	1: a dependency is missing
# 	2: virtualenv is already set up

# check if virtualenv is installed and in $PATH
(which virtualenv > /dev/null) ||
	(	echo You do not have virtualenv installed! Do that!
		exit 1
	)

# check that python3 is installed
(which python3 > /dev/null) ||
	(	echo "You do not have Python 3 installed*"
		echo "*Some distros (such as Arch) use 3 as the default, instead of 2."
		echo "On these distros, you can either modify this shell script to bypass the -"
		echo "python3 check or create a symlink from /usr/bin/python to /usr/bin/python3"
		exit 1
	)

# check that we don't already have one
if [ -d venv ]; then
	echo You already have a virtualenv set up, nuke that if you want to reinstall
	exit 2
fi

# make and load the virtualenv
virtualenv -p $(which python3) venv
. venv/bin/activate

# install all dependecy python packages from list
for pak in $(cat data/technical.d/pip3-packages.txt); do
	pip3 install $pak
done
