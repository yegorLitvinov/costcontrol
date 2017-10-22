.PHONY: deploy

isort:
	isort -rc backend/

create-prod-requirements:
	mkdir -p requirements
	pipenv lock -r > requirements/prod.txt

precommit: isort create-prod-requirements

init-server:
	cd deploy && ansible-playbook init.yml

deploy:
	cd deploy && ansible-playbook deploy.yml


# Commands for production container

gunicorn:
	pip install -r requirements/prod.txt
	cd backend && gunicorn config.wsgi

migrate:
	python backend/manage.py migrate

create-db:
	python backend/manage.py sqlcreate | psql -U postgres -h postgres 2>/dev/null

collectstatic:
	python backend/manage.py collectstatic

yarn:
	yarn
	yarn run build
