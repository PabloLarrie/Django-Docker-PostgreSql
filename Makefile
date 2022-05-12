chown:
	sudo chown `whoami` -R .

up:
	docker-compose up

build:
	docker-compose build

migrate:
	docker-compose run api python manage.py migrate

migrations:
	docker-compose run api python manage.py makemigrations

empty_db:
	docker-compose run api python manage.py flush

charge_csv:
	docker-compose run api python manage.py csv_ingestion

restart_db: empty_db  charge_csv

shell:
	docker-compose run api python manage.py shell

setup: build migrate charge_csv
