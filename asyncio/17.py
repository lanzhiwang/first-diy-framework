#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

import time

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]

start = now()

loop = asyncio.get_event_loop()

'''
future对象有几个状态：Pending、Running、Done、Cancelled
创建future的时候，task为pending，
事件循环调用执行的时候当然就是running，
调用完毕自然就是done，
如果需要停止事件循环，就需要先把task取消，此时任务就是Cancelled状态

启动事件循环之后，马上ctrl+c，会触发run_until_complete的执行异常 KeyBorardInterrupt。
然后通过循环asyncio.Task取消future。
'''
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
    # 可以使用asyncio.Task获取事件循环的task
    print("stop loop!")
    print(asyncio.Task.all_tasks())
    for task in asyncio.Task.all_tasks():
        print(task)
        print(task.cancel()) # True表示cannel成功，：
    loop.stop()
    # loop.run_forever() # loop stop之后还需要再次开启事件循环，最后在close，不然还会抛出异常
finally:
    loop.close()

print('TIME: ', now() - start)

'''
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ python3 17.py 
Waiting:  1
Waiting:  2
Waiting:  4
^Cstop loop!
{<Task pending coro=<wait() running at /usr/lib/python3.5/asyncio/tasks.py:347> wait_for=<Future pending cb=[Task._wakeup()]> cb=[_run_until_complete_cb() at /usr/lib/python3.5/asyncio/base_events.py:164]>, <Task pending coro=<do_some_work() running at 17.py:12> wait_for=<Future pending cb=[Task._wakeup()]> cb=[_wait.<locals>._on_completion() at /usr/lib/python3.5/asyncio/tasks.py:414]>, <Task pending coro=<do_some_work() running at 17.py:12> wait_for=<Future pending cb=[Task._wakeup()]> cb=[_wait.<locals>._on_completion() at /usr/lib/python3.5/asyncio/tasks.py:414]>, <Task pending coro=<do_some_work() running at 17.py:12> wait_for=<Future pending cb=[Task._wakeup()]> cb=[_wait.<locals>._on_completion() at /usr/lib/python3.5/asyncio/tasks.py:414]>}
<Task pending coro=<wait() running at /usr/lib/python3.5/asyncio/tasks.py:347> wait_for=<Future pending cb=[Task._wakeup()]> cb=[_run_until_complete_cb() at /usr/lib/python3.5/asyncio/base_events.py:164]>
True
<Task pending coro=<do_some_work() running at 17.py:12> wait_for=<Future pending cb=[Task._wakeup()]> cb=[_wait.<locals>._on_completion() at /usr/lib/python3.5/asyncio/tasks.py:414]>
True
<Task pending coro=<do_some_work() running at 17.py:12> wait_for=<Future pending cb=[Task._wakeup()]> cb=[_wait.<locals>._on_completion() at /usr/lib/python3.5/asyncio/tasks.py:414]>
True
<Task pending coro=<do_some_work() running at 17.py:12> wait_for=<Future pending cb=[Task._wakeup()]> cb=[_wait.<locals>._on_completion() at /usr/lib/python3.5/asyncio/tasks.py:414]>
True
TIME:  0.5883784294128418
Task was destroyed but it is pending!
task: <Task pending coro=<do_some_work() done, defined at 17.py:10> wait_for=<Future cancelled> cb=[_wait.<locals>._on_completion() at /usr/lib/python3.5/asyncio/tasks.py:414]>
Task was destroyed but it is pending!
task: <Task pending coro=<do_some_work() done, defined at 17.py:10> wait_for=<Future cancelled> cb=[_wait.<locals>._on_completion() at /usr/lib/python3.5/asyncio/tasks.py:414]>
Task was destroyed but it is pending!
task: <Task pending coro=<do_some_work() done, defined at 17.py:10> wait_for=<Future cancelled> cb=[_wait.<locals>._on_completion() at /usr/lib/python3.5/asyncio/tasks.py:414]>
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ 

'''
