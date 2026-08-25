import asyncio

async def fetch_data(source_id, delay):
    await asyncio.sleep(delay)
    return f"Data from source {source_id}"


async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(fetch_data(1, 0.1))
        t2 = tg.create_task(fetch_data(2, 0.2))
    print(t1.result(), t2.result())


if __name__ == "__main__":
    asyncio.run(main())