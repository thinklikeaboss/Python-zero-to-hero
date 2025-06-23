# src/chapter5.py

"""
Chapter 5 – Control Flow
Author: Luca Bocaletto
Description: Demonstrate Python's control flow constructs:
             conditionals (if/elif/else), loops (for, while),
             and loop controls (break, continue).
"""

def demo_conditionals():
    print("== Conditional Statements ==")
    x = 10
    if x < 5:
        print("x is less than 5")
    elif x < 15:
        print("x is between 5 and 14")
    else:
        print("x is 15 or more")

    # Nested example
    score = 85
    if score >= 90:
        grade = "A"
    else:
        if score >= 80:
            grade = "B"
        else:
            grade = "C"
    print(f"Score: {score} → Grade: {grade}\n")

def demo_for_loops():
    print("== for Loops ==")
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(f"Fruit: {fruit}")

    print("\nUsing range():")
    for i in range(5):
        print(i, end=" ")
    print("\n")

    print("With enumerate():")
    for idx, val in enumerate(fruits, start=1):
        print(f"{idx}. {val}")
    print()

def demo_while_loops():
    print("== while Loops ==")
    count = 0
    while count < 3:
        print(f"Count is {count}")
        count += 1

    print("\nSentinel loop:")
    running = True
    while running:
        cmd = input("Enter command (quit to exit): ")
        if cmd.lower() == "quit":
            running = False
        else:
            print("You typed:", cmd)
    print()

def demo_break_continue():
    print("== break & continue ==")
    print("break example:")
    for n in range(10):
        if n == 5:
            print("Breaking at", n)
            break
        print(n, end=" ")
    print("\n")

    print("continue example:")
    for n in range(5):
        if n % 2 == 0:
            continue
        print(n, end=" ")
    print("\n")

def main():
    print("\n=== Chapter 5: Control Flow Demo ===\n")
    demo_conditionals()
    demo_for_loops()
    demo_while_loops()
    demo_break_continue()
    print("=== End of Chapter 5 ===\n")

if __name__ == "__main__":
    main()
