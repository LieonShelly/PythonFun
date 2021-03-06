from ProxyPool.DB import RedisClient
from ProxyPool.Crawler import Crawler
from ProxyPool.Setting import *
import sys

class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()


    def isOverThreshold(self):
        print(type(self.redis.count))
        if self.redis.count() > POOL_UPPER_THRESHOLD:
            return True
        else:
            return False
        
    def run(self):
        if not self.isOverThreshold():
            for callbackLabel in range(self.crawler.__CrawlFuncCount__):
                print('*****', callbackLabel)
                callback = self.crawler.__CrawlFunc__[callbackLabel]

                proxies = self.crawler.getProxies(callback)
                sys.stdout.flush()
                for proxy in proxies:
                    self.redis.add(proxy)