# coding = utf-8
import asyncio


async def hello():
    print("Hello world!")
    await asyncio.sleep(1)
    print("Hello again!")


def main01():
    loop = asyncio.get_event_loop()
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


main01()
