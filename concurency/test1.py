import asyncio
from typing import Optional

import aiohttp
from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str, delay: int = 0) -> Optional[int]:
    try:
        ten_millis = aiohttp.ClientTimeout(total=100)
        async with session.get(url, timeout=ten_millis) as result:

            status = result.status
            await asyncio.sleep(delay)
            return status
    except Exception as e:
        print(f"Exception: {e}")
        raise e


async def main():
    connector = aiohttp.TCPConnector(limit=10)
    session_timeout = aiohttp.ClientTimeout(connect=.1)
    async with aiohttp.ClientSession(connector=connector, timeout=session_timeout) as session:
        pending = [
            asyncio.create_task(fetch_status(session, 'http://httpbin.org/status/200', 1)) for _ in range(100)
        ]

        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED, timeout=2)

            print(f'Done task count: {len(done)}')
            print(f'Pending task count: {len(pending)}')

            for done_task in done:
                if done_task.exception() is None:
                    result = done_task.result()
                    if result is not None:
                        print(result)
                    else:
                        print("log to elastic: No result")
                else:
                    print("log to elastic: Exception occurred")

asyncio.run(main())
