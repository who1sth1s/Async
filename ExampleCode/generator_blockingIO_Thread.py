import timeit
# futures explain : http://i5on9i.blogspot.kr/2016/07/python-future.html
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen

urls = ['https://google.com', 'https://www.apple.com', 'http://www.naver.com']

def fetch(url):
    print('Start : ', url)  # return : start url
    urlopen(url)
    print('Done : ', url)  # return : done url

start = timeit.default_timer()

# with explain : http://soooprmx.com/wp/archives/4079
with ThreadPoolExecutor(max_workers=5) as executor:
    for url in urls:
        executor.submit(fetch, url)

duration = timeit.default_timer() - start
print(duration)  # return : 0.48097191299893893 ~ 0.5646912950032856
