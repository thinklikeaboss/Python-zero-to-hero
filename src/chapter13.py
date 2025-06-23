# src/chapter13.py

"""
Chapter 13 – Concurrency & Parallelism
Author: Luca Bocaletto
Description:
    Demonstrate Python's threading, multiprocessing,
    concurrent.futures (ThreadPoolExecutor & ProcessPoolExecutor),
    and asyncio for asynchronous I/O.
"""

import threading
import time
from multiprocessing import Process, Pool
import concurrent.futures
import asyncio

# Shared state for threading demo
counter = 0
counter_lock = threading.Lock()

def worker_thread(n):
    """Simple thread worker that sleeps then prints."""
    print(f"[Thread-{n}] starting")
    time.sleep(0.5)
    print(f"[Thread-{n}] done")

def safe_increment():
    """Increment the global counter safely under a lock."""
    global counter
    with counter_lock:
        tmp = counter
        tmp += 1
        time.sleep(0.01)  # simulate work
        counter = tmp

def demo_threading():
    print("== threading Demo ==")
    # 1) basic threads
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker_thread, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Basic threading complete\n")

    # 2) safe counter increment
    global counter
    counter = 0
    threads = []
    for _ in range(10):
        t = threading.Thread(target=safe_increment)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Final counter value (should be 10): {counter}\n")

def worker_process(n):
    """Process worker that sleeps then prints."""
    print(f"[Process-{n}] starting")
    time.sleep(0.5)
    print(f"[Process-{n}] done")

def demo_multiprocessing():
    print("== multiprocessing Demo ==")
    # 1) individual processes
    procs = []
    for i in range(2):
        p = Process(target=worker_process, args=(i,))
        procs.append(p)
        p.start()
    for p in procs:
        p.join()
    print("Individual processes complete\n")

    # 2) pool of workers
    def square(x):
        return x * x

    with Pool(4) as pool:
        results = pool.map(square, [1, 2, 3, 4])
    print("Pool results:", results, "\n")

def demo_futures():
    print("== concurrent.futures Demo ==")
    def square(x):
        return x * x

    # ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        thread_results = list(executor.map(square, range(5)))
    print("ThreadPoolExecutor results:", thread_results)

    # ProcessPoolExecutor
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        proc_results = list(executor.map(square, range(5)))
    print("ProcessPoolExecutor results:", proc_results, "\n")

async def say_after(delay, msg):
    """Coroutine that waits then prints a message."""
    await asyncio.sleep(delay)
    print(msg)

async def demo_asyncio():
    print("== asyncio Demo ==")
    # schedule two coroutines concurrently
    task1 = asyncio.create_task(say_after(1, "-- hello after 1s"))
    task2 = asyncio.create_task(say_after(2, "++ world after 2s"))
    print("Tasks started")
    await task1
    await task2
    print("asyncio demo complete\n")

def main():
    print("\n=== Chapter 13: Concurrency & Parallelism Demo ===\n")
    demo_threading()
    demo_multiprocessing()
    demo_futures()
    # run the asyncio part
    asyncio.run(demo_asyncio())
    print("=== End of Chapter 13 ===\n")

if __name__ == "__main__":
    main()
