import asyncio
import aiohttp
from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str, delay: int = 0) -> int:
    async with session.get(url) as result:
        a = result.status
        await asyncio.sleep(delay)
        return a


async def main():
    async with aiohttp.ClientSession() as session:
        pending = [
            asyncio.create_task(fetch_status(session, 'http://httpbin.org/status/400', 10)),
            asyncio.create_task(fetch_status(session, 'http://httpbin.org/status/200', 1)),
            asyncio.create_task(fetch_status(session, 'http://httpbin.org/status/404', 1)),
        ]

        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED, timeout=2)
            print(f'Done task count: {len(done)}')
            print(f'Pending task count: {len(pending)}')
            for done_task in done:
                # result = await done_task
                if done_task.exception() is None:
                    print(done_task.result())
                else:
                    print("log to elastic")


asyncio.run(main())
