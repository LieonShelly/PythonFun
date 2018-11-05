import asyncio
import aiohttp
import time
import sys
try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError
from ProxyPool.DB import RedisClient
from ProxyPool.Setting import *


class Tester(object):
    def __init__(self):
        self.redis = RedisClient()
    
    async def testSignleProxy(self, proxy):
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                realProxy = "http://" + proxy
                print('Testing:', proxy)
                async with session.get(TEST_URL, proxy=realProxy, timeout=15, allow_redirects=False) as response:
                    if response.status in VALID_STATUS_CODES:
                        self.redis.max(proxy)
                    else:
                        self.redis.decrease(proxy)
                        print('请求响应码不合法 ', response.status, 'IP', proxy)
            except (ClientError, aiohttp.client_exceptions.ClientConnectorError, asyncio.TimeoutError, AttributeError):
                self.redis.decrease(proxy)
                print('代理请求失败', proxy)

    def run(self):
        try:
            count = self.redis.count()
            for i in range(0, count, BATCH_TEST_SIZE):
                start = i
                stop = min(i+BATCH_TEST_SIZE, count)
                print('正在测试第', start + 1, '-', stop, '个代理')
                testProxies = self.redis.batch(start, stop)
                loop = asyncio.get_event_loop()
                tasks = [(self.testSignleProxy(proxy)) for proxy in testProxies ]
                loop.run_until_complete(asyncio.wait(tasks))
                sys.stdout.flush()
                time.sleep(5)
        except Exception as e:
            print('测试器发生错误', e.args)