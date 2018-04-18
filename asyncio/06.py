#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import asyncio

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    return 'Done after {}s'.format(x)

def callback(future):
    print('Callback: ', future.result())


start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)

'''
绑定回调，在task执行完毕的时候可以获取执行的结果，回调的最后一个参数是future对象，
通过该对象可以获取协程返回值。如果回调需要多个参数，可以通过偏函数导入。
可以看到，coroutine执行结束时候会调用回调函数。并通过参数future获取协程执行的结果。
我们创建的task和回调里的future对象，实际上是同一个对象。
'''
task.add_done_callback(callback)
loop.run_until_complete(task)

print('TIME: ', now() - start)

'''
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ python3 06.py 
Waiting:  2
Callback:  Done after 2s
TIME:  0.0009047985076904297
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ 

'''