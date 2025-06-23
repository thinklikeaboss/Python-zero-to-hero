# src/chapter11.py

"""
Chapter 11 – Object-Oriented Programming
Author: Luca Bocaletto
Description: Demonstrate Python's OOP features:
             defining classes, instance & class members,
             inheritance & polymorphism, special methods,
             and encapsulation with @property.
"""

def demo_classes_instances():
    print("== Classes & Instances ==")
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            return f"Hello, I'm {self.name} and I'm {self.age}."

    alice = Person("Alice", 30)
    bob = Person("Bob", 25)
    print(alice.greet())
    print(bob.greet())
    print()

def demo_class_members():
    print("== Instance vs Class Members ==")
    class Counter:
        total_instances = 0           # class variable

        def __init__(self):
            Counter.total_instances += 1
            self.id = Counter.total_instances

        def instance_info(self):
            return f"Instance ID: {self.id}"

        @classmethod
        def how_many(cls):
            return f"Total instances: {cls.total_instances}"

        @staticmethod
        def description():
            return "Counter class counts its own instances."

    c1 = Counter()
    c2 = Counter()
    print(c1.instance_info())
    print(c2.instance_info())
    print(Counter.how_many())
    print("Static:", Counter.description())
    print()

def demo_inheritance_polymorphism():
    print("== Inheritance & Polymorphism ==")
    class Animal:
        def speak(self):
            raise NotImplementedError("Subclasses must implement speak()")

    class Dog(Animal):
        def speak(self):
            return "Woof!"

    class Cat(Animal):
        def speak(self):
            return "Meow!"

    pets = [Dog(), Cat()]
    for pet in pets:
        print(pet.__class__.__name__, "says", pet.speak())
    print()

def demo_special_methods():
    print("== Special Methods (Dunder) ==")
    class Point:
        def __init__(self, x, y):
            self.x, self.y = x, y

        def __repr__(self):
            return f"Point({self.x}, {self.y})"

        def __str__(self):
            return f"({self.x}, {self.y})"

        def __eq__(self, other):
            if not isinstance(other, Point):
                return NotImplemented
            return (self.x, self.y) == (other.x, other.y)

        def __add__(self, other):
            if not isinstance(other, Point):
                return NotImplemented
            return Point(self.x + other.x, self.y + other.y)

    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(3, 4)
    print("repr:", repr(p1))
    print("str: ", str(p1))
    print("p1 == p2:", p1 == p2)
    print("p1 + p3:", p1 + p3)
    print()

def demo_encapsulation_properties():
    print("== Encapsulation & @property ==")
    class Account:
        def __init__(self, balance):
            self.__balance = balance    # private attribute

        @property
        def balance(self):
            """The account balance (read-only)."""
            return self.__balance

        @balance.setter
        def balance(self, amount):
            if amount < 0:
                raise ValueError("Balance cannot be negative")
            self.__balance = amount

        def deposit(self, amt):
            self.balance += amt

        def withdraw(self, amt):
            self.balance -= amt

    acct = Account(100)
    print("Initial balance:", acct.balance)
    acct.deposit(50)
    print("After deposit:", acct.balance)
    try:
        acct.withdraw(200)
    except ValueError as e:
        print("Error:", e)
    print("Final balance remains:", acct.balance)
    print()

def main():
    print("\n=== Chapter 11: OOP Demo ===\n")
    demo_classes_instances()
    demo_class_members()
    demo_inheritance_polymorphism()
    demo_special_methods()
    demo_encapsulation_properties()
    print("=== End of Chapter 11 ===\n")

if __name__ == "__main__":
    main()
