import time
from multiprocessing import Process
from ProxyPool.Api import app
from ProxyPool.Getter import Getter
from ProxyPool.Tester import Tester
from ProxyPool.DB import RedisClient
from ProxyPool.Setting import *

class Scheduler():
    def scheduleTester(self, cycle=TESTER_CYCLE):
        tester = Tester()
        while True:
            print('Tester is running')
            tester.run()
            time.sleep(cycle)

    def scheduleGetter(self, cycle=GETTER_CYCLE):
        getter = Getter()
        while True:
            print('Getter is running')
            getter.run()
            time.sleep(cycle)
    
    def schduleApi(self):
        app.run(API_HOST, API_PORT)

    def run(self):
        print('Proxy is running')
        if TESTER_ENABLED:
            testerProcess = Process(target=self.scheduleTester)
            testerProcess.start()
        if GETTER_ENABLED:
            testerProcess = Process(target=self.scheduleGetter)
            testerProcess.start()
        if API_ENABLED:
            testerProcess = Process(target=self.schduleApi)
            testerProcess.start()
