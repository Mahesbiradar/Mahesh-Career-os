
# 1. Threading Fundamentals

"""
downloading 3 files in sequntial manner may take 6 second in total + overhead. If we use threading for the same it may reduce the total time to 2 sec + overhead. Therefor threads are suitable for the i/o bound works. Here is code template for the above application.

"""
# import threading

# import time


# def download_file(file_id):
  
#     print(f"started downloading the file with id: {file_id}")
#     time.sleep(2)
#     print(f"The file {file_id} is downloaded")

# start = time.perf_counter()

# download_file1 = threading.Thread(target=download_file, args=[101])
# download_file2 = threading.Thread(target=download_file, args=[102])
# download_file3 = threading.Thread(target=download_file, args=[103])

# download_file1.start()
# download_file2.start()
# download_file3.start()

# # download_file1.join()
# # download_file2.join()
# # download_file3.join()

# end = time.perf_counter()


# print(f"The taken for downloading all the files {round(end-start,2)} sec")




# 2. ThreadPoolExecutor & Futures


# import concurrent.futures
# import requests

# import time

# urls = [
#     "https://httpbin.org",
#     "https://httpbin.org",
#     "https://typicode.com",
#     "https://typicode.com",
#     "https://reqres.in",
#     "https://google.com",
#     "https://bing.com",
#     "https://wikipedia.org",
#     "https://github.com",
#     "https://appspot.com"
# ]


# def fetch_url(url):

#     try:
#         responce = requests.get(url, timeout=5)

#         return url, responce.status_code

#     except Exception as e:

#         return url, f"Error: {e}"

# start_time = time.time()


# with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:

#     results = executor.map(fetch_url, urls)


# for url,status in results:

#     print(f"{url} -> Status: {status}")

# print(f"\nTotal time taken: {time.time() - start_time:.2f} seconds")


"""
The Main diffrence between is that map() is high level and ordered, while submit() is the low level and dynamic.

The o/p order is trictly preserved in map() and in submit its out of order

the return value of map() is an iterator yeilding the actull results directly. in submit retunrs a A Future object (a promise of a future result)

"""


# 3. Multiprocessing & the GIL

# import concurrent.futures

# import time

# def sum_of_squares(n):

#     result = 0

#     for num in range(1,n+1):

#         result += num**2

#     return result

# numbers = [10000000, 20000000, 30000000, 40000000]

# if __name__ == "__main__":

#     start = time.perf_counter()

#     with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:

#         results = executor.map(sum_of_squares, numbers)


#     print(list(results))

#     end = time.perf_counter()

#     print(f"Time Taken: {round(end-start,2)} sec")


"""
For the CPU Bound works the multiprocessing is effeicent where the processes were runnung in the CPU and in parrall cores which lifts heavy computation and which reduces the Time.

GIL Is the Global interpreter look which allows threads to execute one at time.

Creating the processe for the tiny work is not worthwhile beacuse the overhead to setup and cleanup the process takes more time than executing the tiny work sequeceilly.

"""


# 4. Asyncio Fundamentals


# What happens when an async function is called?

"""
When we call a function defined with async def. it doesnot executes any code in the function body, instead it return the a specialized object called coroutine.
Its bluprint of the work to be done.
"""


# What does await do?

"""
The await keyword does two critical things:

1: passes control: it yeilds control of the execution back to the event loop. it tells the loop "im waiting for this external operation to finish. Go run other tasks in the meantime."

2.Pauses and Resumes: it pauses the current coroutine at that exact line. Once the awaited operation completes, the Event Loop wakes this coroutine up and resumes it with the returned result.

"""

# What is the Event Loop responsible for?

"""
The event loop the engine of the any asynchronous application. it runs continuously on a single thread and is responsible for:

Keeping track of all running, paused, and pending tasks.

Giving the CPU back to paused coroutines the moment their awaited data becomes available.

"""


# Coroutine is A function object returned by calling an async def function. It is passive and won't run until explicitly awaited or scheduled.


# Tass is A wrapper that registers a coroutine with the Event Loop so it can run in the background. It is active.


# Future is A low-level object representing an execution that has not finished yet, but promises a result down the road.


# import asyncio
# import time

# async def fetch_data(id, delay):
#     print(f"Task {id}: Starting data fetch...")
#     await asyncio.sleep(delay) 
#     print(f"Task {id}: Data fetched!")
#     return f"Data {id}"

# async def main():
#     start_time = time.perf_counter()
    
#     task1 = asyncio.create_task(fetch_data(1, 2.0))
#     task2 = asyncio.create_task(fetch_data(2, 1.0))
    
  
#     res1 = await task1
#     res2 = await task2
    
#     end_time = time.perf_counter()
#     print(f"Results: {res1}, {res2}")
#     print(f"Total execution time: {round(end_time - start_time, 2)} seconds")

# if __name__ == "__main__":
#     asyncio.run(main())


# 5. Sequential vs Concurrent Async I/O



import asyncio

import time



async def fetch_record(record_id):

    print(f"Fetching record {record_id}...")

    await asyncio.sleep(2)
    print(f"Finished fetching record {record_id}!")

    return f"Record {record_id} Data"


async def run_sequentially():
    print("\n--- Starting Sequential Run ---")
    start = time.perf_counter()

    res1 = await fetch_record(1)
    res2 = await fetch_record(2)
    res3 = await fetch_record(3)

    end = time.perf_counter()
    print(f"Sequential Time Taken: {round(end - start, 2)} seconds")
    return [res1, res2, res3]

async def run_concurrently():
    print("\n--- Starting Concurrent Run ---")
    start = time.perf_counter()

    results = await asyncio.gather(
        fetch_record(1),
        fetch_record(2),
        fetch_record(3)
    )

    end = time.perf_counter()
    print(f"Concurrent Time Taken: {round(end - start, 2)} seconds")
    return results

async def main():
    await run_sequentially()
    await run_concurrently()

if __name__ == "__main__":
    asyncio.run(main())


# 6. Blocking vs Non-blocking & Backend Use


# time.sleep(2) freezes the entire thread. Because the event loop runs on a single thread, the entire application halts and no other coroutine can run.

# await asyncio.sleep(2) yields control. It tells the event loop, "I am idling for 2 seconds; go run other coroutines in the meantime."


# use asyncio.to_thread() it to run legacy, blocking synchronous code (like standard file operations, requests.get(), or synchronous database drivers) inside an async app. It offloads the blocking work to a background thread so the event loop doesn't freeze.

# (a) Many compatible network requests \(\rightarrow \) asyncio
# Network calls are I/O-bound (mostly waiting). asyncio efficiently handles thousands of concurrent connections on a single thread without the heavy memory overhead of creating thousands of OS threads.

# (b) Heavy pure-Python CPU calculations \(\rightarrow \) multiprocessing
# Calculations are CPU-bound. Because the GIL prevents multiple threads from executing Python code at the same time, you must use separate processes (multiprocessing) to achieve true parallel execution across multiple CPU cores.