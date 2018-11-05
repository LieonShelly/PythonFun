import redis
from random import choice
import re
from ProxyPool.Setting import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_KEY
from ProxyPool.Setting import MAX_SCORE, MIN_SCORE, INITIAL_SCORE
from ProxyPool.Error import PoolEmptyError

class RedisClient():
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
    
    def add(self, proxy, score=INITIAL_SCORE):
        if not re.match('\d+\.\d+\.\d+\.\d+\:\d+', proxy):
            print('not a valid proxy', proxy, 'abandan')
            return
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, score, proxy)
    
    def random(self):
        result = self.db.zrangebyscore(REDIS_KEY,MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                 raise PoolEmptyError
    
    def decrease(self, proxy):
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('proxy', proxy, 'current score', score, 'decrease 1')
            return self.db.zincrby(REDIS_KEY, proxy, -1)
        else:
            print('proxy', proxy, 'current score', score, 'remove')
            return self.db.zrem(REDIS_KEY, proxy)
    
    def exists(self, proxy):
        return not self.db.zscore(REDIS_KEY, proxy) == None


    def max(self, proxy):
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def count(self):
        return self.db.zcard(REDIS_KEY)
    
    def all(self):
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)

    def batch(self, start, stop):
        return self.db.zrevrange(REDIS_KEY, start, stop - 1)

    if __name__ == '__main__':
        conn = RedisClient()
        result = conn.batch(680, 688)
        print(result)