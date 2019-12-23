init:
	sudo apt-get update
	sudo apt-get install python3-dev
	sudo apt-get install python3-pip
	sudo pip3 install -r requirements.txt --no-cache-dir
	sudo apt-get install supervisor
	sudo cp supervisor.conf /etc/supervisor/conf.d
	sudo service supervisor reread
	sudo service supervisor update
