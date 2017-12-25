# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
import asyncio
import datetime


async def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        # print(loop.time())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # Blocking call which returns when the display_date() coroutine is done
    loop.run_until_complete(display_date(loop))
    loop.close()
