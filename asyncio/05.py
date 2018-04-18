#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import time

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)


start = now()

coroutine = do_some_work(2)

loop = asyncio.get_event_loop()

'''
协程对象不能直接运行，在注册事件循环的时候，其实是run_until_complete方法将协程包装成为了一个任务（task）对象。
所谓task对象是Future类的子类。保存了协程运行后的状态，用于未来获取协程的结果。
'''

'''
将协程包装成为了一个任务的方法
asyncio.ensure_future(coroutine) 和 loop.create_task(coroutine)都可以创建一个task，
run_until_complete的参数是一个futrue对象。当传入一个协程，其内部会自动封装成task，
task是Future的子类。isinstance(task, asyncio.Future)将会输出True。
'''
# task = asyncio.ensure_future(coroutine)
task = loop.create_task(coroutine)
print(task) # Task pending状态

loop.run_until_complete(task)

print(task) # Task finished状态

print('TIME: ', now() - start)

'''
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ python3 05.py 
<Task pending coro=<do_some_work() running at 05.py:9>>
Waiting:  2
<Task finished coro=<do_some_work() done, defined at 05.py:9> result=None>
TIME:  0.001178741455078125
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ 

'''
