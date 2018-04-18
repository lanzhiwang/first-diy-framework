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
    
    # 如果使用的是 asyncio.gather创建协程对象，那么await的返回值就是协程运行的结果。
    results = await asyncio.gather(*tasks)

    for result in results:
        print('Task ret: ', result)


start = now()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

print('TIME: ', now() - start)

'''
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ python3 12.py 
Waiting:  1
Waiting:  2
Waiting:  4
Task ret:  Done after 1s
Task ret:  Done after 2s
Task ret:  Done after 4s
TIME:  4.004920959472656
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ 


'''
