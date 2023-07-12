#create by 6310301006 Nanthana Howong

# example of waiting for all tasks to complete
import random
import asyncio
import time

# coroutine for a task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random.random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'{time.ctime()} >task {arg} done with {value}')

# main coroutine 
async def main():
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for all tasks to complete # ALL_COMPLETED, FIRST_EXCEPTION
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    # report its details
    print(f'{time.ctime()} All done')


# start the asyncio program
asyncio.run(main())

#
# Wed Jul 12 15:02:22 2023 >task 6 done with 0.0792413462055136
# Wed Jul 12 15:02:22 2023 >task 5 done with 0.2536128268035134
# Wed Jul 12 15:02:22 2023 >task 3 done with 0.36589170142775784
# Wed Jul 12 15:02:22 2023 >task 9 done with 0.3997874009612573
# Wed Jul 12 15:02:22 2023 >task 0 done with 0.49598589939525495
# Wed Jul 12 15:02:22 2023 >task 8 done with 0.6063792514069869
# Wed Jul 12 15:02:22 2023 >task 1 done with 0.6393414237883905
# Wed Jul 12 15:02:22 2023 >task 7 done with 0.7454643906299384
# Wed Jul 12 15:02:22 2023 >task 2 done with 0.8590711239011566
# Wed Jul 12 15:02:22 2023 >task 4 done with 0.8754474798596872
# Wed Jul 12 15:02:22 2023 All done

#
# Wed Jul 12 15:03:17 2023 >task 5 done with 0.14580383562598231
# Wed Jul 12 15:03:17 2023 >task 1 done with 0.15556908938433667
# Wed Jul 12 15:03:17 2023 All done