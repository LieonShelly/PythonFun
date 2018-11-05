from flask import Flask, g
from ProxyPool.DB import RedisClient

__all__ = ['app']

app = Flask(__name__)

def getConn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    return 'ProxyPool'

@app.route('/random')
def getRandom():
    conn = getConn()
    return conn.random()

@app.route('/count')
def getCount():
    conn = getConn()
    return str(conn.count())


if __name__ == '__main__':
    app.run()