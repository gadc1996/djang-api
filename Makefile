app:
	cd src && \
	python manage.py startapp $(name)

## Django
migrations:
	python src/manage.py makemigrations
	
migrate:
	python src/manage.py migrate

serve:
	python src/manage.py runserver

update-dependencies:
	pip3 freeze > requirements.txt

install:
	pip install $(name)
	make update-dependencies

setup:
	pip3 install -r requirements.txt
	
superuser:
	python src/manage.py createsuperuser
	
shell:
	python src/manage.py shell
	
test:
	python src/manage.py test $(name)

## Elastic Beanstalk
eb-init:
	eb init -p docker $$EB_APP_NAME

create:
    eb create $$EB_ENV_NAME

eb-create:
    eb create <your-environment-name>

eb-deploy:
    eb deploy

eb-terminate:
    eb terminate <your-environment-name>
