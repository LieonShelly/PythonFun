from app import celery
from celery.schedules import crontab
from app.task import task_api
import time
from flask import jsonify

@celery.task(name='task.add')
def add(x, y):
	return x + y

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
	sender.add_periodic_task(50.0, test.s('hello'), name='add every 10')
	sender.add_periodic_task(60.0, test.s('world'), expires=10)
	sender.add_periodic_task(
		crontab(hour=7, minute=30, day_of_week=1),
		test.s('happy Monday'),
	)


@celery.task(name='task.test')
def test(arg):
	print(arg)

@task_api.route('/')
def index():
	long_time_work(20)
	return "index DONE"

@task_api.route('/work')
def work():
	return "work DONE"

@celery.task(name='task.long_time_work')
def long_time_work(how_long=5):
	time.sleep(how_long)
	print("DONE")
	return "long time work!"
