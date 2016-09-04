import timeit
from urllib.request import urlopen

urls = ['https://google.com', 'https://www.apple.com', 'http://www.naver.com']
start = timeit.default_timer()

for url in urls:
    print('start : ', url)  # return : start url
    urlopen(url)
    print('done : ', url)  # return : done url

duration = timeit.default_timer() - start
print(duration)  # return : 1.1181397679974907 ~ 1.1369662829965819
