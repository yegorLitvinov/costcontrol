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


backup_dump:
	mkdir -p backup
	ssh $(HOST) "docker exec costcontrol_postgres_1 bash -c 'pg_dump -U postgres -Fc costcontrol > /var/lib/postgresql/data/costcontrol.dump'"
	rsync -aP --delete -e ssh $(HOST):$(PROJECT_SRC)/deploy/postgres/volume/costcontrol.dump $(DST)/backup/costcontrol.dump

restore_dump:
	 pg_restore -Fc -cv -W -d costcontrol -U costcontrol -h localhost backup/costcontrol.dump

backup_json:
	mkdir -p backup
	ssh $(HOST) "docker exec costcontrol_web_1 bash -c 'python backend/manage.py dumpdata > /srv/costcontrol/backup/costcontrol.json'"
	rsync -aP --delete -e ssh $(HOST):$(PROJECT_SRC)/backup/costcontrol.json $(DST)/backup/costcontrol.json

restore_json:
	 django-admin loaddata $(DST)/backup/costcontrol.json

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
