# -*- coding: utf-8 -*-
import timeit
from concurrent.futures import ProcessPoolExecutor
from urllib.request import urlopen

urls = ['https://google.com', 'https://www.apple.com', 'http://www.naver.com']

def fetch(url):
    print('start : ' + url)  # return : start url
    urlopen(url)
    print('done : ' + url)  # return : done url

start = timeit.default_timer()
with ProcessPoolExecutor(max_workers=5) as executor:
    for url in urls:
        executor.submit(fetch, url)

duration = timeit.default_timer() - start  # return : 0.5519957579963375~0.9513322269922355
print(duration)

# 직접적인 메모리 공유 X
# No GIL, CPU-bound 유리
# high cost, big overhead
# CPU 중심 프로세스(CPU bound ) : 연산에 더 많은 시간 소비
