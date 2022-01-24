#
# [mst] multitask.py 
# playing around with multitasking
#
# log:
# - 2020.12 initial
# - scheduler module
#

import sched
import time

import asyncio # asynchronous functionality

async def as_f():
    print ("hi, i'm an async function")

# a scheduler will need a timing and a delaying functions on initialization
s = sched.scheduler(time.time, time.sleep)

# delay, priority, function to run and arguments
s.enter(0, 11, print, argument=('first',))
s.enter(5, 2, print, argument=('second',))
s.enter(3, 6, print, argument=('third',))


asyncio.run(as_f()) # this will appear asynchronously before the above stuff


# run the tasks
s.run()
