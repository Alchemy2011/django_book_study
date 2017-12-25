# -*- coding: utf-8 -*-
# __author__ = 'liqirong'


def reader():
    """A generator that fakes a read from a file, socket, etc"""
    for i in range(4):
        yield '<< %d' % i


def reader_wrapper(g):
    yield from g

if __name__ == '__main__':
    wrap = reader_wrapper(reader())
    for i in wrap:
        print(i)

"""
import asyncio


@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print("Hello again!")

if __name__ == '__main__':
    # 获取EventLoop
    loop = asyncio.get_event_loop()
    # 执行coroutine
    loop.run_until_complete(hello())
    loop.close()
"""

"""
import asyncio

async def hello_world():
    print("Hello World!")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # Blocking call which returns when the hello_world() coroutine is done
    loop.run_until_complete(hello_world())
    loop.close()
"""
