.PHONY: deploy backup
HOST=root@195.201.27.44
PROJECT_SRC=/home/costcontrol/costcontrol
DST=$(realpath ./)
NOW=$(shell date +%Y-%m-%d_%H-%M)

isort:
	isort -rc backend

black:
	black -l 90 backend

flake:
	flake8 backend locustfile.py

create-requirements:
	mkdir -p requirements
	pipenv lock -r > requirements/prod.txt
	pipenv lock -r > requirements/dev.txt
	sort requirements/prod.txt -o requirements/prod.txt
	sort requirements/dev.txt -o requirements/dev.txt

pre-commit: isort black flake create-requirements

hook:
	echo "make pre-commit" > .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit

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
	ssh $(HOST) "sudo su postgres -c 'pg_dump costcontrol > /tmp/costcontrol.sql'"
	rsync -aP --delete -e ssh $(HOST):/tmp/costcontrol.sql $(DST)/backup/costcontrol.sql

restore:
	psql -d costcontrol -U costcontrol -h localhost -f backup/costcontrol.sql
