init:
	sudo apt-get install supervisor
	sudo apt-get install python3-dev
	sudo apt-get install python3-pip
	sudo apt-get install python3-virtualenv
	sudo pipenv shell
	sudo pip3 install -r requirements.txt --no-cache-dir
	sudo cp uni.conf /etc/supervisor/conf.d/
	sudo supervisorctl reread
	sudo supervisorctl update
