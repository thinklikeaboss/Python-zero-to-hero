# src/chapter9.py

"""
Chapter 9 – Errors & Exceptions
Author: Luca Bocaletto
Description:
    Demonstrate Python's error handling:
    - SyntaxError vs runtime exceptions
    - try/except/else/finally blocks
    - raising exceptions
    - defining and catching custom exceptions
    - using assert for sanity checks
"""

import os

def demo_errors_vs_exceptions():
    print("== Errors vs Exceptions ==")
    # SyntaxError example via exec
    bad_code = 'print "Missing parentheses"'  # invalid in Python 3
    try:
        exec(bad_code)
    except SyntaxError as e:
        print("Caught SyntaxError:", e)
    # Runtime exception
    try:
        _ = 1 / 0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)
    print()

def demo_try_except():
    print("== try / except Demo ==")
    test_values = ["abc", "0", "5"]
    for s in test_values:
        print(f"Input: {s!r}")
        try:
            num = int(s)
            result = 10 / num
        except ValueError:
            print("  ValueError: could not convert to int")
        except ZeroDivisionError:
            print("  ZeroDivisionError: division by zero")
        else:
            print("  Success:", result)
    print()

def demo_else_finally():
    print("== else & finally Demo ==")
    fname = "demo_ch9.txt"
    # create a small file
    with open(fname, "w", encoding="utf-8") as f:
        f.write("demo line\n")
    f = None
    try:
        f = open(fname, "r", encoding="utf-8")
        content = f.read()
    except FileNotFoundError:
        print("  FileNotFoundError: file not found")
    else:
        print("  File content:", content.strip())
    finally:
        if f:
            f.close()
            print("  File closed in finally block")
    # cleanup
    os.remove(fname)
    print()

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return True

def demo_raising():
    print("== Raising Exceptions Demo ==")
    for age in (25, -10):
        try:
            print(f"check_age({age}) →", check_age(age))
        except ValueError as e:
            print("  Caught ValueError:", e)
    print()

class InvalidConfigError(Exception):
    """Raised when a configuration dict is invalid."""
    pass

def load_config(cfg):
    if "host" not in cfg:
        raise InvalidConfigError("Missing 'host' key")
    return cfg["host"]

def demo_custom_exceptions():
    print("== Custom Exceptions Demo ==")
    good = {"host": "localhost"}
    bad = {}
    for cfg in (good, bad):
        try:
            host = load_config(cfg)
            print("  Loaded host:", host)
        except InvalidConfigError as e:
            print("  Caught InvalidConfigError:", e)
    print()

def factorial(n):
    assert n >= 0, "n must be non-negative"
    return 1 if n in (0, 1) else n * factorial(n - 1)

def demo_assertions():
    print("== Assertions Demo ==")
    for n in (3, -1):
        try:
            print(f"factorial({n}) →", factorial(n))
        except AssertionError as e:
            print("  AssertionError:", e)
    print()

def main():
    print("\n=== Chapter 9: Errors & Exceptions Demo ===\n")
    demo_errors_vs_exceptions()
    demo_try_except()
    demo_else_finally()
    demo_raising()
    demo_custom_exceptions()
    demo_assertions()
    print("=== End of Chapter 9 ===\n")

if __name__ == "__main__":
    main()
