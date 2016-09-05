import aiohttp
import asyncio
import timeit

@asyncio.coroutine
def fetch(url):
    print('start : ' + url)  # return : start url
    req = yield from aiohttp.request('GET', url)
    print('done : ' + url)  # return : done url

@asyncio.coroutine
def fetch_all(urls):
    # generator object rapping to asyncio.Task
    fetches = [asyncio.Task(fetch(url)) for url in urls]
    # wait all of coroutine Task and gather all result and return
    yield from asyncio.gather(*fetches)

urls = ['https://google.com', 'https://www.apple.com', 'http://naver.com']

start = timeit.default_timer()
# create event loop(execute fetch_all)
# Insert function generator into event loop queue
asyncio.get_event_loop().run_until_complete(fetch_all(urls))
duration = timeit.default_timer() - start
print(duration)
