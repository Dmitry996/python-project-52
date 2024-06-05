run:
	python3 manage.py runserver

start:
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi