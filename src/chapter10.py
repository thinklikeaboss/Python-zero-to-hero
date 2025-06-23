# src/chapter10.py

"""
Chapter 10 – Iterators, Generators & Comprehensions
Author: Luca Bocaletto
Description: Demonstrate Python's iteration protocol,
             custom iterator classes, generator functions,
             generator expressions, and comprehensions.
"""

def demo_iterators():
    print("== Iterators & Protocol ==")
    nums = [10, 20, 30]
    it = iter(nums)
    print("Using next():", next(it), next(it), next(it))
    try:
        next(it)
    except StopIteration:
        print("StopIteration raised when exhausted")
    print()

    class Counter:
        def __init__(self, limit):
            self.limit = limit
            self.cur = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self.cur >= self.limit:
                raise StopIteration
            val = self.cur
            self.cur += 1
            return val

    print("Custom Counter(3):", list(Counter(3)))
    print()

def demo_generators():
    print("== Generator Functions ==")
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    print("fib(6):", end=" ")
    for num in fib(6):
        print(num, end=" ")
    print("\n")

def demo_genexpr():
    print("== Generator Expressions ==")
    gen = (x * x for x in range(5))
    print("next(gen):", next(gen))
    print("Remaining:", list(gen))
    print()

def demo_comprehensions():
    print("== Comprehensions ==")
    # list comprehension
    evens = [x for x in range(10) if x % 2 == 0]
    print("List of evens 0–9:", evens)

    # dict comprehension
    sq_map = {x: x * x for x in range(6)}
    print("Dict of squares 0–5:", sq_map)

    # set comprehension
    names = ["Alice", "Bob", "Anna"]
    initials = {name[0] for name in names}
    print("Set of initials:", initials)
    print()

def main():
    print("\n=== Chapter 10: Iterators, Generators & Comprehensions Demo ===\n")
    demo_iterators()
    demo_generators()
    demo_genexpr()
    demo_comprehensions()
    print("=== End of Chapter 10 ===\n")

if __name__ == "__main__":
    main()
