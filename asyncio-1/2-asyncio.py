#create by 6310301006 Nanthana Howong

# example of getting the current task from the main coroutine
import asyncio
import time

# define a main coroutine
async def main():
    # report a message
    print(f'{time.ctime()} main coroutine started')
    # get the current task
    task = asyncio.current_task()
    # report its details
    print(f'{time.ctime()} {task}')

# start the asyncio program
asyncio.run(main())

#
#Wed Jul 12 14:20:25 2023 main coroutine started
#Wed Jul 12 14:20:25 2023 <Task pending name='Task-1' coro=<main() running at C:\Users\User\Downloads\asyncio-1\
# 2-asyncio.py:14> cb=[_run_until_complete_cb() at C:\Users\User\AppData\Local\Programs\Python\Python310\lib\
# asyncio\base_events.py:184]>