# src/chapter2.py

"""
Chapter 2 – Data Types & Variables
Author: Luca Bocaletto
Description: Demonstrate Python's core data types, variable assignment, mutability.
"""

def show_type(name, val):
    """Print variable name, its value, and its type."""
    print(f"{name} = {val!r} (type: {type(val).__name__})")

def main():
    # 1. Core data types
    print("== Core Data Types ==")
    show_type("integer_literal", 123)
    show_type("float_literal", 3.14)
    show_type("string_literal", "Hello, World")
    show_type("boolean_literal", True)
    show_type("none_literal", None)

    # 2. Variable assignment
    print("\n== Variable Assignment ==")
    age = 30
    name = "Alice"
    height = 1.65
    is_student = False
    no_value = None

    show_type("age", age)
    show_type("name", name)
    show_type("height", height)
    show_type("is_student", is_student)
    show_type("no_value", no_value)

    # 3. Reassignment
    print("\n== Reassignment ==")
    age = "thirty"
    show_type("age (reassigned)", age)

    # 4. Mutability vs Immutability
    print("\n== Mutability Demo ==")
    # Mutable: list
    items = [1, 2, 3]
    show_type("items before", items)
    items.append(4)
    show_type("items after append", items)

    # Immutable: tuple
    coords = (10, 20)
    show_type("coords", coords)
    try:
        coords[0] = 0
    except TypeError as e:
        print(f"Error: cannot modify tuple -> {e}")

    # Immutable: string
    text = "immutable"
    show_type("text", text)
    try:
        text[0] = "I"
    except TypeError as e:
        print(f"Error: cannot modify string -> {e}")

if __name__ == "__main__":
    main()
