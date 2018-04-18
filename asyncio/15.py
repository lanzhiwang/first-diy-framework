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

    # 使用asyncio的as_completed方法
    for task in asyncio.as_completed(tasks):
        result = await task
        print('Task ret: {}'.format(result))

start = now()

loop = asyncio.get_event_loop()
done = loop.run_until_complete(main())

print('TIME: ', now() - start)

'''
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ python3 15.py 
Waiting:  1
Waiting:  2
Waiting:  4
Task ret: Done after 1s
Task ret: Done after 2s
Task ret: Done after 4s
TIME:  4.005694150924683
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ 


'''
