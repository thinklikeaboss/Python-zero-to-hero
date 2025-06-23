# src/chapter16.py

"""
Chapter 16 – Decorators & Context Managers
Author: Luca Bocaletto
Description:
    Demonstrate Python's first-class functions, closures,
    simple and parameterized decorators, custom context managers
    via __enter__/__exit__, and generator-based managers with contextlib.
"""

from contextlib import contextmanager
import time

# 1. Closures & Inner Functions
def make_multiplier(factor):
    """Return a function that multiplies its input by the given factor."""
    def multiply(x):
        return x * factor
    return multiply

def demo_closures():
    print("== Closures Demo ==")
    times3 = make_multiplier(3)
    times5 = make_multiplier(5)
    print("3 * 10 =", times3(10))
    print("5 * 7  =", times5(7))
    print()

# 2. Simple Decorator
def debug(func):
    """A decorator that logs calls and returned values."""
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[DEBUG] {func.__name__} returned {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

def demo_simple_decorator():
    print("== Simple Decorator Demo ==")
    add(2, 5)
    print()

# 3. Parameterized Decorator
def repeat(n):
    """Decorator factory that repeats function call n times."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(1, n+1):
                print(f"[repeat {i}/{n}]")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

def demo_param_decorator():
    print("== Parameterized Decorator Demo ==")
    greet("Alice")
    print()

# 4. Class-Based Context Manager
class Resource:
    """A simple resource manager using __enter__ and __exit__."""
    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        # suppress exceptions if needed; here we don't
        return False

def demo_class_context_manager():
    print("== Class-Based Context Manager Demo ==")
    with Resource() as r:
        print("  Using resource inside with-block")
    print()

# 5. Generator-Based Context Manager
@contextmanager
def open_file(path, mode):
    """Yield a file object and ensure it's closed afterwards."""
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()

def demo_contextlib_manager():
    print("== contextlib Context Manager Demo ==")
    fname = "temp_demo.txt"
    with open_file(fname, "w") as f:
        f.write("Hello, context manager!")
    with open_file(fname, "r") as f:
        content = f.read()
        print("  Read content:", content)
    # cleanup
    import os
    os.remove(fname)
    print()

def main():
    print("\n=== Chapter 16: Decorators & Context Managers Demo ===\n")
    demo_closures()
    demo_simple_decorator()
    demo_param_decorator()
    demo_class_context_manager()
    demo_contextlib_manager()
    print("=== End of Chapter 16 ===\n")

if __name__ == "__main__":
    main()
