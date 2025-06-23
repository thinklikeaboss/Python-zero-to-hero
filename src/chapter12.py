# src/chapter12.py

"""
Chapter 12 – Debugging, Logging & Testing
Author: Luca Bocaletto
Description: 
    Demonstrate Python debugging techniques (print, pdb),
    logging configuration and usage,
    and use of assert for sanity checks.
"""

import pdb
import logging

def compute(x, y):
    """
    A simple function that divides x by y,
    with a debug print to inspect inputs.
    """
    print(f"DEBUG compute(): x={x}, y={y}")
    return x / y

def buggy():
    """
    An intentionally buggy function. 
    You can step through this with pdb.set_trace().
    """
    a = 1
    pdb.set_trace()    # breakpoint for interactive debugging
    b = 0
    return a / b

def divide(a, b):
    """
    Divide two numbers with an assertion to prevent zero-division.
    Raises AssertionError if b == 0.
    """
    assert b != 0, "b must not be zero"
    return a / b

def demo_debugging():
    print("== Debugging Demo ==")
    # 1) print-based inspection
    try:
        result = compute(10, 2)
        print("Result:", result)
        result = compute(5, 0)
        print("Result:", result)
    except Exception as e:
        print("Caught exception during compute():", e)

    # 2) interactive pdb demo (uncomment to use)
    # buggy()
    print("To debug 'buggy()', uncomment the call to buggy() above and run this script.")
    print()

def demo_logging():
    print("== Logging Demo ==")
    # configure root logger
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )
    logger = logging.getLogger(__name__)

    logger.debug("This is a debug message")
    logger.info("Informational message")
    logger.warning("Warning: something might be wrong")
    logger.error("Error encountered")
    print()

def demo_assertions():
    print("== Assertions Demo ==")
    tests = [(8, 2), (8, 0)]
    for a, b in tests:
        try:
            print(f"divide({a}, {b}) =", divide(a, b))
        except AssertionError as e:
            print("  AssertionError:", e)
    print()

def main():
    print("\n=== Chapter 12: Debugging, Logging & Testing Demo ===\n")
    demo_debugging()
    demo_logging()
    demo_assertions()
    print("=== End of Chapter 12 ===\n")

if __name__ == "__main__":
    main()
