from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import  time
import datetime
from  datetime import  date
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


# scheduler = BlockingScheduler()
#
# def job1():
# 	print("excute" + time.asctime())
#
# scheduler.add_job(job1, 'interval', seconds=3)
# scheduler.start()
# # 一次性指定日期
# scheduler.add_job(job1, 'date', run_date=date(2019,9,9))
# scheduler.add_job(job1, 'date', run_date=datetime(2019,2,3,21,23,3))
# scheduler.add_job(job1, 'date', run_date='2019-9-2 21:30:05')
#
# # 间隔调度
# scheduler = BackgroundScheduler()
# scheduler.add_job(job1, 'interval', hours=2)
# scheduler.add_job('cron', month='1-12', day='3rd fri', hour='0-3')
# scheduler.add_job(job1, day_of_week='mon-fri', hour=5, minute=30, end_date='2019-12-31')

jobstores = {
	'mongo': MongoDBJobStore(),
	'default': MongoDBJobStore()
}

excuters = {
	'default': ThreadPoolExecutor(20),
	'processpool': ProcessPoolExecutor(5)
}

job_defaults = {
	'coalesce': False,
	'max_instance': 3
}

scheduler = BackgroundScheduler(jobstores=jobstores, excuters=excuters, job_defaults=job_defaults)
# scheduler.add_job(job1, day_of_week='mon-sun', hours=0, minute=0, id='my_job1')
# scheduler.start()
# scheduler.remove_job('my_job_id')
# scheduler.get_jobs()
# scheduler.shutdown()

@scheduler.scheduled_job("interval",seconds=1)
def rebate():
	print("Schedule execute")

if __name__ == '__main__':

	try:
		scheduler.start()
	except:
		scheduler.shutdown()