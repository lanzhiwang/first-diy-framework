#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

import time

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    # 不在main协程函数里处理结果，直接返回await的内容，那么最外层的run_until_complete将会返回main协程的结果
    return await asyncio.gather(*tasks)

start = now()

loop = asyncio.get_event_loop()
results = loop.run_until_complete(main())

for result in results:
    print('Task ret: ', result)

print('TIME: ', now() - start)

'''
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ python3 13.py 
Waiting:  1
Waiting:  2
Waiting:  4
Task ret:  Done after 1s
Task ret:  Done after 2s
Task ret:  Done after 4s
TIME:  4.005758047103882
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ 


'''
