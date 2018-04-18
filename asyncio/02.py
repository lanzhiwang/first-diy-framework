#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import asyncio

@asyncio.coroutine
def hello1():
    print('Hello world1! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again1! (%s)' % threading.currentThread())

@asyncio.coroutine
def hello2():
    print('Hello world2! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again2! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello1(), hello2()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

'''
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ python3 02.py 
Hello world2! (<_MainThread(MainThread, started 140010002700032)>)
Hello world1! (<_MainThread(MainThread, started 140010002700032)>)
等待一秒
Hello again2! (<_MainThread(MainThread, started 140010002700032)>)
Hello again1! (<_MainThread(MainThread, started 140010002700032)>)
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ 
'''