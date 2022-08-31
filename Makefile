export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_TYPE=en_US.UTF-8

help:
	@echo "Makefile for swinemovement-ms"
	@echo "\033[33;36m"
	@echo "Production commands:"
	@echo "buildapp		Builds a docker image of the app"
	@echo "startapp		Starts all services necessary for app. Webserver on 9113"
	@echo "stopapp			Stops all services"
	@echo "migrate			Run Postgres DB migration"
	@echo "loaddata		Load dummmy data. Will error out if data already exists"
	@echo "admin			Create Admin creds"
	@echo "restartapp		Restarts webserver"
	@echo
	@echo "Dev commands:"
	@echo "dev_first_init       	Install required packages, start infra components, add db schema and dummy data"
	@echo "dev_init             	Install required packages and start infra components."
	@echo "dev_runserver        	Run Django server @9113"
	@echo "dev_runshell         	Run Django shell"

buildapp:
	sudo docker build --file ./app/Dockerfile -t swinemovementms:1.0.0 ./app

startapp:
	sudo docker-compose -f ./infra/docker-compose.yml up -d
	sudo docker exec -it infra_web_1 python3 manage.py collectstatic --noinput

stopapp:
	sudo docker-compose -f ./infra/docker-compose.yml down

migrate:
	sudo docker exec -it infra_web_1 python3 manage.py migrate

loaddata:
	sudo docker exec -it infra_web_1 python3 manage.py loaddata

admin:
	sudo docker exec -it infra_web_1 python3 manage.py createsuperuser

restartapp:
	sudo docker restart infra_web_1

dev_first_init:
	@echo "!! WARNING !! Please activate python virtual environment"
	@echo "Recommended to use python 3.8"
	sleep 5
	pip3 install -r ./app/requirements/production.txt
	sudo docker-compose -f ./infra/docker-compose.yml up -d postgres redis
	sleep 5
	python3 ./app/manage.py migrate
	python3 ./app/manage.py loaddata
	@echo "Create Admin User"
	python3 ./app/manage.py createsuperuser

dev_init:
	@echo "!! WARNING !! Please activate python virtual environment"
	@echo "Recommended to use python 3.8"
	sleep 5
	pip3 install -r ./app/requirements/production.txt
	sudo docker-compose -f ./infra/docker-compose.yml up -d postgres redis

dev_runserver:
	python3 ./app/manage.py runserver 9113

dev_runshell:
	python3 ./app/manage.py shell
