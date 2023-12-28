import time
import asyncio

import aiohttp
from aiohttp import ClientSession

# ذخیره زمان‌های آخرین timeout یا خطای 500 هر دامنه
last_error_time = {}


async def wait_for_retry(url: str):
    # چک کردن زمان آخرین timeout یا خطای 500 برای این دامنه
    last_error = last_error_time.get(url, 0)
    current_time = time.time()
    if current_time - last_error < 1800:  # اگر آخرین خطا در مدت ۳۰ دقیقه اخیر بوده است
        wait_time = int(1800 - (current_time - last_error))
        print(f"Waiting for {wait_time} seconds due to recent errors.")
        await asyncio.sleep(wait_time)


async def fetch_status(session: ClientSession, url: str, delay: int = 0, timeout: int = 5, max_retries: int = 3) -> int:
    await wait_for_retry(url)

    try:
        result = await asyncio.wait_for(session.get(url), timeout=timeout)
        a = result.status
        await asyncio.sleep(delay)
        return a
    except aiohttp.ClientError as e:
        print(f"Error: {e}")
        last_error_time[url] = time.time()
        # تاخیر یک مدت مشخص (به عنوان مثال، 30 دقیقه)
        print(f"Retrying in {1800} seconds...")
        await wait_for_retry(url)
        return await fetch_status(session, url, delay, timeout, max_retries - 1)


async def main():
    async with aiohttp.ClientSession() as session:
        pending = [
            asyncio.create_task(fetch_status(session, 'http://httpbin.org/status/400', 10)),
            asyncio.create_task(fetch_status(session, 'http://httpbin.org/status/200', 1)),
            asyncio.create_task(fetch_status(session, 'http://httpbin.org/status/404', 1)),
        ]

        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
            print(f'Done task count: {len(done)}')
            print(f'Pending task count: {len(pending)}')
            for done_task in done:
                if done_task.exception() is None:
                    print(done_task.result())
                else:
                    print("log to elastic")
                    # اگر درخواست به دلیل timeout یا خطای 500 نتواست انجام شود، دوباره اجرا شود
                    pending.add(asyncio.create_task(done_task))


asyncio.run(main())
