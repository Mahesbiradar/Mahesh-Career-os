# Part A — Threading and Multiprocessing
import time

import threading

start = time.perf_counter()

def download_file(file_id):
    print(f"Starting download {file_id}.")
    time.sleep(2)
    print(f"Finished download {file_id}.")


t1 = threading.Thread(target=download_file,args=[1])
t2 = threading.Thread(target=download_file,args=[2])
t3 = threading.Thread(target=download_file,args=[3])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


end = time.perf_counter()

print(f"elapsed time:{end-start}")




# Exercise 2 — ThreadPoolExecutor



import time

import concurrent.futures

start = time.perf_counter()

def download_file(file_id):
    print(f"Starting download {file_id}.")
    time.sleep(2)
    print(f"Finished download {file_id}.")

files =range(1,10)

with concurrent.futures.ThreadPoolExecutor() as executor:

    results = executor.map(download_file,files)


end = time.perf_counter()

print(f"elapsed time:{end-start}")




# Exercise 3 — ProcessPoolExecutor

import time

import concurrent.futures



def sum_of_squares(n):

    print(f"Starting computing: {n}")
    result = 0

    for num in range(1,n+1):

        result = num*2

    return result


if __name__ == "__main__":

    start = time.perf_counter()

    numbers = [1000, 2000, 3000, 4000]

    with concurrent.futures.ProcessPoolExecutor() as executor:

        results = executor.map(sum_of_squares,numbers)


    print(list(results))

    end = time.perf_counter()

    print(f"Elapsed time: {end - start:.2f} seconds")




# Part B — Asyncio


# Exercise 4 — async / await

import asyncio

import time

async def fetch_record(record_id):

    print(f"Fecthing record with id: {record_id}")

    await asyncio.sleep(2)

    return f"Record {record_id} fetched."


async def main():

    start = time.perf_counter()

    res1 = await fetch_record(1)
    res2 = await fetch_record(2)
    res3 = await fetch_record(3)

    results = [res1,res2,res3]
    print(results)

    end = time.perf_counter()

    print(f"Elapsed time: {end - start:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())



# Exercise 5 — Concurrent asyncio tasks


import asyncio

import time

async def fetch_record(record_id):

    print(f"Fecthing record with id: {record_id}")

    await asyncio.sleep(2)

    return f"Record {record_id} fetched."


async def main():

    start = time.perf_counter()


    results = await asyncio.gather(
        fetch_record(1),
        fetch_record(2),
        fetch_record(3)
        )

    print(results)

    end = time.perf_counter()

    print(f"Elapsed time: {end - start:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())


# Exercise 6 — Blocking vs non-blocking

# Version 1: Put time.sleep(2) inside worker_a().

import time 

import asyncio

async def worker_a():
    print("Worker A: Starting a heavy 2-second task (Blocking)...")
    time.sleep(2)
    print("Worker A: Finished task.")

async def worker_b():

    for i in range(5):

        print(f"Worker B: Running iteration {i}...")

    await asyncio.sleep(0.1)


async def main():

    await asyncio.gather(worker_a(),worker_b())

if __name__ == "__main__":
    asyncio.run(main())


# Version 2: Replace it with await asyncio.sleep(2).

import time 

import asyncio

async def worker_a():
    print("Worker A: Starting a heavy 2-second task (Blocking)...")
    await asyncio.sleep(2)
    print("Worker A: Finished task.")

async def worker_b():

    for i in range(5):

        print(f"Worker B: Running iteration {i}...")

    await asyncio.sleep(0.1)


async def main():

    await asyncio.gather(worker_a(),worker_b())

if __name__ == "__main__":
    asyncio.run(main())
    









    