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

    # 返回使用asyncio.wait方式挂起协程
    return await asyncio.wait(tasks)


start = now()

loop = asyncio.get_event_loop()
done, pending = loop.run_until_complete(main())

for task in done:
    print('Task ret: ', task.result())

print('TIME: ', now() - start)

'''
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ python3 14.py 
Waiting:  1
Waiting:  2
Waiting:  4
Task ret:  Done after 2s
Task ret:  Done after 4s
Task ret:  Done after 1s
TIME:  4.004699945449829
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ 

'''
