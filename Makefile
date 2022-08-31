export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_TYPE=en_US.UTF-8

help:
	@echo "Makefile for swinemovement-ms"
	@echo "\033[33;36m"
	@echo "first-init       Install required packages, start infra components, add db schema and dummy data "
	@echo "init             Install required packages and start infra components."
	@echo "runserver                Run django server @9113"
	@echo "runshell         Run django shell"
	@echo "stopinfra         Stops supporting infra docker components"

first_init:
	@echo "!! WARNING !! Please activate python virtual environment"
	@echo "Recommended to use python 3.8"
	sleep 5
	pip3 install -r ./app/requirements/production.txt
	sudo docker-compose -f ./infra/docker-compose.yml up -d
	sleep 5
	python3 ./app/manage.py migrate
	python3 ./app/manage.py loaddata
	@echo "Create Admin User"
	python3 ./app/manage.py createsuperuser

init:
	@echo "!! WARNING !! Please activate python virtual environment"
	@echo "Recommended to use python 3.8"
	sleep 5
	pip3 install -r ./app/requirements/production.txt
	sudo docker-compose -f ./infra/docker-compose.yml up -d

runserver:
	python3 ./app/manage.py runserver 9113

runshell:
	python3 ./app/manage.py shell

stopinfra:
	sudo docker-compose -f ./infra/docker-compose.yml down

