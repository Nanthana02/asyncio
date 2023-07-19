#create by 6310301006 Nanthana Howong

# example of an asynchronous iterator with async for loop
import asyncio
import time

# define an asynchronous iterator
class AsyncTterator():
    # constructor, define some state
    def __init__(self):
        self.counter = 0

    # create an instance of the iterator
    def __aiter__(self):
        return self
    
    # return the next awaitable
    async def __anext__(self):
        # check for no fortune items
        if self.counter >= 10:
            raise StopAsyncIteration
        # increment the counter
        self.counter += 1
        # simulate work
        await asyncio.sleep(1)
        # return the counter value
        return self.counter
    
# main coroutine
async def main():
    # loop over async iterator with async for loop
    async for item in AsyncTterator():
        print(f'{time.ctime()} {item}')
# excute the asyncio program
asyncio.run(main())


# Wed Jul 19 13:49:16 2023 1
# Wed Jul 19 13:49:17 2023 2
# Wed Jul 19 13:49:18 2023 3
# Wed Jul 19 13:49:19 2023 4
# Wed Jul 19 13:49:20 2023 5
# Wed Jul 19 13:49:21 2023 6
# Wed Jul 19 13:49:22 2023 7
# Wed Jul 19 13:49:23 2023 8
# Wed Jul 19 13:49:24 2023 9
# Wed Jul 19 13:49:25 2023 10