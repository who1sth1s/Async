import asyncio
import datetime
import timeit

async def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

start = timeit.default_timer()
asyncio.get_event_loop().run_until_complete(display_date())
duration = timeit.default_timer() - start
print(duration)


# Can't understand