# src/chapter4.py

"""
Chapter 4 – Console I/O
Author: Luca Bocaletto
Description: Demonstrate Python's console input/output:
             print(), input(), and string formatting techniques.
"""

import sys

def demo_print():
    print("== print() Demo ==")
    # default separator and newline
    print("Hello", "World")               # Hello World
    # custom end (no newline)
    print("No newline", end="")
    print(" → same line")
    # custom separator and flush
    print(1, 2, 3, sep=" - ")             # 1 - 2 - 3
    print("Immediate output", flush=True)
    print()

def demo_input():
    print("== input() Demo ==")
    # reading strings
    name = input("Enter your name: ")
    age_str = input("Enter your age: ")
    try:
        age = int(age_str)
        print(f"Hello, {name}! You are {age} years old.")
    except ValueError:
        print("Error: age must be a number.")
    print()

def demo_formatting():
    print("== String Formatting Demo ==")
    user = "Alice"
    score = 95.6789

    # a) f-strings (Python 3.6+)
    print(f"F-string: {user} scored {score:.2f} points")

    # b) str.format()
    template = "{0} has {1} new messages"
    print("format(): " + template.format(user, 5))

    # c) % operator
    fmt = "percent %: %s achieved %d%% accuracy"
    print(fmt % (user, 88))
    print()

def main():
    print("\n=== Chapter 4: Console I/O Demo ===\n")
    demo_print()
    demo_input()
    demo_formatting()
    print("=== End of Chapter 4 ===\n")

if __name__ == "__main__":
    main()
