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
    coroutine3 = do_some_work(2)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    done, pending = await asyncio.wait(tasks)

    for task in done:
        print('Task ret: ', task.result())

start = now()

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(main())
'''
循环task，逐个cancel是一种方案，
可是正如上面我们把task的列表封装在main函数中，main函数外进行事件循环的调用。
这个时候，main相当于最外出的一个task，那么处理包装的main函数即可。
'''
try:
    loop.run_until_complete(task)
except KeyboardInterrupt as e:
    print(asyncio.Task.all_tasks())
    print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()

'''
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ python3 18.py 
Waiting:  1
Waiting:  2
Waiting:  2
^C{<Task pending coro=<main() running at 18.py:26> wait_for=<Future pending cb=[Task._wakeup()]> cb=[_run_until_complete_cb() at /usr/lib/python3.5/asyncio/base_events.py:164]>, <Task pending coro=<do_some_work() running at 18.py:12> wait_for=<Future pending cb=[Task._wakeup()]> cb=[_wait.<locals>._on_completion() at /usr/lib/python3.5/asyncio/tasks.py:414]>, <Task pending coro=<do_some_work() running at 18.py:12> wait_for=<Future pending cb=[Task._wakeup()]> cb=[_wait.<locals>._on_completion() at /usr/lib/python3.5/asyncio/tasks.py:414]>, <Task pending coro=<do_some_work() running at 18.py:12> wait_for=<Future pending cb=[Task._wakeup()]> cb=[_wait.<locals>._on_completion() at /usr/lib/python3.5/asyncio/tasks.py:414]>}
True
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ 

'''

