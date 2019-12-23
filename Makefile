init:
	sudo apt-get install python3-dev
	sudo apt-get install python3-pip
	sudo apt-get install gunicorn3
	sudo apt-get install supervisor
	sudo pip3 install pipenv --no-cache-dir
	sudo pipenv install -r requirements.txt
	sudo pipenv shell
	sudo cp uni.conf /etc/supervisor/conf.d/
	sudo supervisorctl reread
	sudo supervisorctl update
