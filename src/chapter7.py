# src/chapter7.py

"""
Chapter 7 – Functions & Modules
Author: Luca Bocaletto
Description: Demonstrate defining functions with various args,
             writing docstrings, using *args/**kwargs,
             and the __name__ == "__main__" idiom.
"""

# 1. Defining Functions
def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"

def power(base, exp=2):
    """Raise base to exp (default=2)."""
    return base ** exp

def demo_defining():
    print("== Defining Functions ==")
    print(greet("Alice"))
    print(f"power(5) = {power(5)}")
    print(f"power(2,3) = {power(2,3)}\n")

# 2. Docstrings & Scope
def add(a, b):
    """
    Add two numbers.

    Args:
        a (int): first operand
        b (int): second operand

    Returns:
        int: sum of a and b
    """
    return a + b

counter = 0

def inc():
    """Increment the global counter by 1."""
    global counter
    counter += 1

def demo_docstrings():
    print("== Docstrings & Scope ==")
    # show docstring
    print("add.__doc__:")
    print(add.__doc__)
    # scope demonstration
    print(f"counter before inc(): {counter}")
    inc()
    print(f"counter after inc():  {counter}\n")

# 3. *args & **kwargs
def summarize(*args):
    """Return the sum of all positional args."""
    return sum(args)

def config(**kwargs):
    """Print key=value pairs passed as keyword args."""
    for key, val in kwargs.items():
        print(f"{key} = {val}")

def mixed(a, *args, **kwargs):
    """Show all kinds of arguments."""
    print("a =", a)
    print("args =", args)
    print("kwargs =", kwargs)

def demo_varargs():
    print("== *args & **kwargs ==")
    print("summarize(1,2,3,4) =", summarize(1,2,3,4))
    print("config(host='localhost', port=8080):")
    config(host="localhost", port=8080)
    print("mixed(1,2,3, x=10, y=20):")
    mixed(1,2,3, x=10, y=20)
    print()

# 4. __name__ & Modules
def demo_modules():
    print("== Modules & __name__ ==")
    if __name__ == "__main__":
        print("This script is run directly ( __name__ == '__main__' ).")
    else:
        print("This script is imported as a module ( __name__ == '__main__' is False ).")
    print()

def main():
    print("\n=== Chapter 7: Functions & Modules Demo ===\n")
    demo_defining()
    demo_docstrings()
    demo_varargs()
    demo_modules()
    print("=== End of Chapter 7 ===\n")

if __name__ == "__main__":
    main()
