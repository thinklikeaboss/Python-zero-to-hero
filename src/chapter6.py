# src/chapter6.py

"""
Chapter 6 – Collections
Author: Luca Bocaletto
Description: Demonstrate Python's built-in collections—
             lists, tuples, sets, dicts—
             plus iteration and comprehensions.
"""

def demo_lists():
    print("== Lists: Creation, Indexing, Methods ==")
    fruits = ["apple", "banana", "cherry"]
    print("Initial:", fruits)

    # Indexing & slicing
    print("First item:", fruits[0])
    print("Slice [1:3]:", fruits[1:3])

    # Common methods
    fruits.append("date")
    print("After append('date'):", fruits)
    fruits.insert(1, "blueberry")
    print("After insert(1,'blueberry'):", fruits)
    fruits.remove("banana")
    print("After remove('banana'):", fruits)
    popped = fruits.pop(2)
    print(f"pop(2) removed '{popped}':", fruits)

    fruits.sort()
    print("After sort():", fruits)
    fruits.reverse()
    print("After reverse():", fruits)
    fruits.extend(["elderberry", "fig"])
    print("After extend([...]):", fruits)
    print()

def demo_tuples():
    print("== Tuples: Immutable Sequences & Unpacking ==")
    coords = (10, 20)
    single = (42,)
    print("coords:", coords, "single:", single)

    # Unpacking
    x, y = coords
    print(f"Unpacked coords -> x={x}, y={y}")

    # Tuples are immutable
    try:
        coords[0] = 0
    except TypeError as e:
        print("Cannot modify tuple:", e)
    print()

def demo_sets():
    print("== Sets: Unordered Unique Collections ==")
    a = {1, 2, 3, 3}
    b = set([3, 4, 5])
    print("Set a (duplicates dropped):", a)
    print("Set b:", b)

    a.add(4)
    print("After a.add(4):", a)
    a.discard(2)
    print("After a.discard(2):", a)

    print("Union a|b:", a | b)
    print("Intersection a&b:", a & b)
    print("Difference a-b:", a - b)
    print("Symmetric difference a^b:", a ^ b)
    print()

def demo_dicts():
    print("== Dicts: Key–Value Mappings ==")
    person = {"name": "Alice", "age": 30}
    print("Initial:", person)

    # Access & modify
    print("person['name']:", person["name"])
    person["city"] = "Rome"
    print("After person['city']='Rome':", person)

    print("Keys:", list(person.keys()))
    print("Values:", list(person.values()))
    print("Items:", list(person.items()))

    # get, pop, update
    print("get('age'):", person.get("age"))
    p = person.pop("age")
    print(f"pop('age') -> {p}, remaining:", person)

    person.update({"age": 31, "occupation": "Engineer"})
    print("After update(...):", person)
    print()

def demo_iteration_comprehensions():
    print("== Iteration & Comprehensions ==")
    nums = list(range(10))
    print("nums:", nums)

    # Iteration
    print("Iterate over nums:")
    for n in nums:
        print(n, end=" ")
    print("\nEnumerate:")
    for i, val in enumerate(nums, 1):
        print(f"{i}:{val}", end=" ")
    print("\nZip with letters:")
    letters = ["a", "b", "c"]
    for n, l in zip(nums, letters):
        print(f"{n}->{l}", end=" ")
    print()

    # List comprehension
    squares = [x*x for x in nums if x % 2 == 0]
    print("Squares of evens:", squares)

    # Nested comprehension
    pairs = [(i, j) for i in [1,2] for j in ['a','b']]
    print("Cartesian pairs:", pairs)

    # Dict comprehension
    sq_map = {x: x*x for x in range(6)}
    print("Dict of squares:", sq_map)
    print()

def main():
    print("\n=== Chapter 6: Collections Demo ===\n")
    demo_lists()
    demo_tuples()
    demo_sets()
    demo_dicts()
    demo_iteration_comprehensions()
    print("=== End of Chapter 6 ===\n")

if __name__ == "__main__":
    main()
