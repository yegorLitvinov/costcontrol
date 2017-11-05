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
	sort requirements/prod.txt -o requirements/prod.txt

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
	ssh $(HOST) "sudo su postgres -c 'pg_dump costcontrol > /tmp/costcontrol.sql'"
	rsync -aP --delete -e ssh $(HOST):/tmp/costcontrol.sql $(DST)/backup/costcontrol.sql

restore:
	 psql -d costcontrol -U costcontrol -h localhost -f backup/costcontrol.sql
