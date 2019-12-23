setup:
	sudo apt-get install python3
	sudo apt-get install python3-dev
	sudo apt-get install python3-pip
	sudo pip3 install pipenv --no-cache-dir
	sudo pipenv install -r requirements.txt
	sudo pipenv shell

start:
	sudo gunicorn3 -w 2 -b :80 app:app
