setup:
	sudo apt-get update
	sudo apt-get install python3-dev
	sudo apt-get install python3-pip
	sudo pip3 install -r requirements.txt --no-cache-dir
	sudo apt-get install supervisor

deploy:
	sudo cp supervisor.conf /etc/supervisor/conf.d
	sudo supervisorctl reread
	sudo supervisorctl update
