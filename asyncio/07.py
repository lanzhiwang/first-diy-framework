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
loop.run_until_complete(task)

print('Task ret: {}'.format(task.result()))
print('TIME: ', now() - start)

'''
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ python3 07.py 
Waiting:  2
Callback:  Done after 2s
TIME:  0.0009047985076904297
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ 

'''