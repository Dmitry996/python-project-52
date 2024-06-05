run:
	python3 manage.py runserver

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT)  task_manager.wsgi