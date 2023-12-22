import asyncio
import time


async def another_message() -> str:
    print("Hello world11111111111111111!")
    await asyncio.sleep(2)
    print("Hello World 22222222222222222!")
    return "Hello World 22222222222222222!"


async def hello_world_message() -> str:
    print("Hello World33333333333333333")
    await asyncio.sleep(5)
    print("Hello World444444444444444444!")
    return "Hello World444444444444444444!"


async def main() -> None:
    a = time.time()
    r1 = asyncio.create_task(hello_world_message())
    r2 = asyncio.create_task(another_message())

    r3 = await r1
    r4 = await r2

    b = time.time() - a
    print(b)
    print(r3)
    print(r4)


def sanother_message() -> str:
    print("Hello world11111111111111111!")
    time.sleep(2)
    return "Hello World 22222222222222222!"


def shello_world_message() -> str:
    print("Hello World33333333333333333")
    time.sleep(5)
    return "Hello World444444444444444444!"


def main2() -> None:
    a = time.time()
    message = shello_world_message()
    message2 = sanother_message()
    b = time.time() - a
    print(b)
    print(message)
    print(message2)


asyncio.run(main())
# main2()
