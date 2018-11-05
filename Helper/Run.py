from ProxyPool.Scheduler import Scheduler
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    try:
        schduler = Scheduler()
        schduler.run()
    except:
        main()


if __name__ == '__main__':
    main()