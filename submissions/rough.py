import asyncio
import time

async def fetch_data(task_id):
    print(f"Starting {task_id}")
    await asyncio.sleep(2)
    return f"Data {task_id}"

async def main():
    start = time.perf_counter()

    result1 = await fetch_data(1)
    result2 = await fetch_data(2)
    result3 = await fetch_data(3)

    print(result1, result2, result3)
    print("Elapsed:", time.perf_counter() - start)

asyncio.run(main())


import asyncio
import time

async def fetch_data(task_id):
    print(f"Starting {task_id}")
    await asyncio.sleep(2)
    return f"Data {task_id}"

async def main():
    start = time.perf_counter()

    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )

    print(results)
    print("Elapsed:", time.perf_counter() - start)

asyncio.run(main())