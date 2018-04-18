#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import asyncio

now = lambda: time.time()

async def do_some_work(x):
    time.sleep(1)
    print('Waiting: ', x)

'''
通过async关键字定义一个协程（coroutine），协程也是一种对象。
协程不能直接运行，需要把协程加入到事件循环（loop），由后者在适当的时候调用协程。
asyncio.get_event_loop方法可以创建一个事件循环，
然后使用run_until_complete将协程注册到事件循环，并启动事件循环。
'''

start = now()

coroutine = do_some_work(2)

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)

print('TIME: ', now() - start)

'''
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ python3 04.py 
Waiting:  2
TIME:  1.0028247833251953
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ 

'''

