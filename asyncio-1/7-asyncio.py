#create by 6310301006 Nanthana Howong

# example of waiting for all tasks to complete
import asyncio
import time

# define a simple asynchronous
async def simple_task(number):
    # block for a moment
    await asyncio.sleep(1)
    # return the argument
    return number

# cancel the given task after a moment
async def cancel_task(task):
    # block for a moment 
    await asyncio.sleep(0.2)
    # cancel the task
    was_canceled = task.cancel()
    print(f'{time.ctime()} canceled: {was_canceled}')

# define a simple coroutine
async def main():
    # create the coroutine
    coro = simple_task(1)
    # create a task
    task = asyncio.create_task(coro)
    # create the shielded task
    shielded = asyncio.shield(task)
    # create the task to cancel the previous task
    asyncio.create_task(cancel_task(task))
    # handle cancellation
    try:
        # await the shielded task
        result = await shielded
        print(f'{time.ctime()} >got; {result}')
    except asyncio.CancelledError:
        print(f'{time.ctime()} shielded  was cancel')
    # wait a moment
    await asyncio.sleep(1)
    # report the details of the tasks
    print(f'{time.ctime()} shielded: {shielded}')
    print(f'{time.ctime()} task: {task}')


# start the asyncio program
asyncio.run(main())


#
# Wed Jul 12 15:30:51 2023 canceled: True
# Wed Jul 12 15:30:51 2023 shielded  was cancel
# Wed Jul 12 15:30:52 2023 shielded: <Future cancelled>
# Wed Jul 12 15:30:52 2023 task: <Task finished name='Task-2' coro=<simple_task() done, 


#เปลี่ยน shielded เป็น task 
# Wed Jul 12 18:46:26 2023 canceled: True
# Wed Jul 12 18:46:26 2023 shielded  was cancel
# Wed Jul 12 18:46:27 2023 shielded: <Future cancelled>
# Wed Jul 12 18:46:27 2023 task: <Task cancelled name='Task-2' coro=<simple_task() done, 