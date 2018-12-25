from gevent import monkey
monkey.patch_all()
from app import create_app

app = create_app()

if __name__ == '__main__':
	print('====')
	app.run(host='localhost', debug=True)