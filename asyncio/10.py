#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
asyncio实现并发，就需要多个协程来完成任务，
每当有任务阻塞的时候就await，然后其他协程继续工作。创建多个协程的列表，然后将这些协程注册到事件循环中。
'''

import asyncio

import time

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

def callback(future):
    print('Callback: ', future.result())


start = now()

coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

task1 = asyncio.ensure_future(coroutine1)
task1.add_done_callback(callback)

task2 = asyncio.ensure_future(coroutine2)
task2.add_done_callback(callback)

task3 = asyncio.ensure_future(coroutine3)
task3.add_done_callback(callback)

tasks = [task1, task2, task3]

loop = asyncio.get_event_loop()

# asyncio.wait(tasks) 也可以使用 asyncio.gather(*tasks) ,前者接受一个task列表，后者接收一堆task。
loop.run_until_complete(asyncio.wait(tasks))

print('TIME: ', now() - start)

'''
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ python3 10.py 
Waiting:  1
Waiting:  2
Waiting:  4
Callback:  Done after 1s
Callback:  Done after 2s
Callback:  Done after 4s
TIME:  4.005341053009033
总时间为4s左右。4s的阻塞时间，足够前面两个协程执行完毕。如果是同步顺序的任务，那么至少需要7s。
此时我们使用了aysncio实现了并发。
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ 


'''