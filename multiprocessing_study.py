# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
import multiprocessing as mp


def foo(queue):
    queue.put('hello')

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
