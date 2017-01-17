import urllib2
import mechanize
from bs4 import BeautifulSoup as bs
import time

import threading
import Queue
import re
import requests

urls = [
    ("https://www.amazon.co.jp/",),
    ("http://www.yahoo.co.jp/",),
    ("http://www.rakuten.co.jp/",),
    ("https://www.python.org/",),
    ("http://zozo.jp/",),
    ("https://www.w3.org/",),
    ("https://www.oracle.com/index.html",),
    ("http://www.adobe.com/",),
    ("http://www.nhk.or.jp/",),
    ("http://sabe.pythonanywhere.com/",)
    # ("https://www.google.co.jp/",), # >> robot preventing the site to be scraped
]

def run_in_threads(target, args_list):
    result = Queue.Queue()
    
    def task_wrapper(*args):
        result.put(target(*args))
    
    threads = [threading.Thread(target=task_wrapper, args=args) for args in args_list]
    for t in threads: 
        t.start()
    for t in threads: 
        t.join()
    return result

def fetch(url):
    try:
        print(re.search('<title>(.+?)</title>', requests.get(url).text, re.M|re.I).group(1))
    except Exception, oO:
        print (oO)
			
if __name__ == "__main__":
    start = time.time()
    run_in_threads(fetch, urls)
    print("--- {} seconds ---".format((time.time() - start)))
