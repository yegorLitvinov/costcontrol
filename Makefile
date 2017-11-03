.PHONY: deploy backup
HOST=root@139.162.149.111
PROJECT_SRC=/home/web/costcontrol
DST=$(realpath ./)
NOW=$(shell date +%Y-%m-%d_%H-%M)

isort:
	isort -rc backend/

create-prod-requirements:
	mkdir -p requirements
	pipenv lock -r > requirements/prod.txt

precommit: isort create-prod-requirements

init-server:
	cd deploy && ansible-playbook init.yml

deploy:
ifndef nobuild
	yarn
	yarn run build
endif
	cd deploy && ansible-playbook deploy.yml

backup:
	mkdir -p backup
	ssh $(HOST) "docker exec costcontrol_postgres_1 bash -c 'pg_dump -U postgres costcontrol > /var/lib/postgresql/data/dump.sql'"
	rsync -aP --delete -e ssh $(HOST):$(PROJECT_SRC)/deploy/postgres/volume/dump.sql $(DST)/backup/dump_$(NOW).sql

# Commands for production container

gunicorn:
	pip install -r requirements/prod.txt
	cd backend && gunicorn config.wsgi

migrate:
	python backend/manage.py migrate

create-db:
	python backend/manage.py sqlcreate | psql -U postgres -h postgres 2>/dev/null

collectstatic:
	python backend/manage.py collectstatic --noinput
