run:
	python3 manage.py runserver

build:
	poetry install

start:
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi
