import requests
from requests.exceptions import ConnectionError

baseHeader = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}

def getPage(url, options = {}):
    headers = dict(baseHeader, **options)
    print('crawling...', url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        print('crawl fail', url)
        return None