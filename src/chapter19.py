# src/chapter19.py

"""
Chapter 19 – Profiling & Performance Optimization
Author: Luca Bocaletto
Description:
    Demonstrate benchmarking with timeit,
    profiling with cProfile & pstats,
    and examples for line_profiler and memory_profiler.
"""

import timeit
import cProfile
import pstats
import io

# 1. timeit demo
def demo_timeit():
    print("== timeit Demo ==")
    stmt = "sum(range(10000))"
    setup = ""
    # run 1000 loops and report total time
    t = timeit.timeit(stmt, setup=setup, number=1000)
    print(f"sum(range(10000)) x1000 → {t:.4f} seconds\n")

# 2. cProfile demo
def work(n: int) -> int:
    total = 0
    for i in range(n):
        total += i * i
    return total

def demo_cprofile():
    print("== cProfile Demo ==")
    pr = cProfile.Profile()
    pr.enable()
    # profile the work function
    _ = work(100000)
    pr.disable()

    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("cumtime")
    ps.print_stats(5)  # top 5 functions
    print(s.getvalue())

# 3. line_profiler example
# To use: install line_profiler and run:
#    kernprof -l -v src/chapter19.py
#
# @profile
# def compute_line_profile():
#     total = 0
#     for i in range(100000):
#         total += i * i
#     return total
#
# if __name__ == "__main__":
#     compute_line_profile()

# 4. memory_profiler example
# To use: install memory_profiler and run:
#    python -m memory_profiler src/chapter19.py
#
# @profile
# def load_data():
#     data = [i for i in range(1000000)]
#     return data
#
# if __name__ == "__main__":
#     load_data()

def main():
    print("\n=== Chapter 19: Profiling & Performance Optimization Demo ===\n")
    demo_timeit()
    demo_cprofile()

    print("For line-by-line profiling, uncomment @profile compute_line_profile()")
    print("and run with kernprof -l -v src/chapter19.py\n")

    print("For memory profiling, uncomment @profile load_data()")
    print("and run with python -m memory_profiler src/chapter19.py\n")
    print("=== End of Chapter 19 ===\n")

if __name__ == "__main__":
    main()
