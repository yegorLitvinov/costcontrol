.PHONY: deploy

isort:
	isort -rc backend/

precommit: isort

init-server:
	cd deploy && ansible-playbook init.yml

deploy:
	cd deploy && ansible-playbook deploy.yml
