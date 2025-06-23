# src/chapter3.py

"""
Chapter 3 – Operators
Author: Luca Bocaletto
Description: Demonstrate Python's operators:
             arithmetic, comparison, logical, assignment,
             precedence, identity & membership.
"""

def demo_arithmetic():
    print("== Arithmetic Operators ==")
    examples = [
        ("2 +  3",   2 + 3),
        ("5 -  1",   5 - 1),
        ("4 *  3",   4 * 3),
        ("7 /  2",   7 / 2),
        ("7 // 2",   7 // 2),
        ("7 %  2",   7 % 2),
        ("2 ** 3",   2 ** 3),
    ]
    for expr, result in examples:
        print(f"{expr:8} → {result}")
    print()

def demo_comparison():
    print("== Comparison Operators ==")
    examples = [
        ("3 == 3",   3 == 3),
        ("4 != 5",   4 != 5),
        ("2 <  5",   2 < 5),
        ("5 >  2",   5 > 2),
        ("3 <= 3",   3 <= 3),
        ("4 >= 2",   4 >= 2),
    ]
    for expr, result in examples:
        print(f"{expr:8} → {result}")
    print()

def demo_logical():
    print("== Logical Operators ==")
    a, b = True, False
    print(f"{a} and {b} → {a and b}")
    print(f"{a} or  {b} → {a or b}")
    print(f"not {a}      → {not a}")
    print()

def demo_assignment():
    print("== Assignment Operators ==")
    x = 10
    print(f"x = {x}")
    x += 5
    print(f"x += 5  → {x}")
    x *= 2
    print(f"x *= 2  → {x}")
    x //= 3
    print(f"x //= 3 → {x}")
    x %= 4
    print(f"x %= 4  → {x}")
    print()

def demo_precedence():
    print("== Precedence & Step-by-Step ==")
    expr = "(3 + 5) * 2 ** 3 / 4 % 3"
    # Breakdown
    step1 = 3 + 5               # 8
    step2 = 2 ** 3              # 8
    step3 = step1 * step2       # 8 * 8 = 64
    step4 = step3 / 4           # 64 / 4 = 16.0
    step5 = step4 % 3           # 16.0 % 3 = 1.0
    print(f"{expr} = {step5}")
    print(f"Steps:")
    print(f"  3 + 5     → {step1}")
    print(f"  2 ** 3    → {step2}")
    print(f"  {step1} * {step2} → {step3}")
    print(f"  {step3} / 4 → {step4}")
    print(f"  {step4} % 3 → {step5}")
    print()

def demo_identity_membership():
    print("== Identity & Membership ==")
    lst1 = [1, 2, 3]
    lst2 = lst1[:]   # shallow copy
    print(f"lst1 is lst2    → {lst1 is lst2}")
    print(f"lst1 == lst2    → {lst1 == lst2}")
    print(f"2 in {lst1}      → {2 in lst1}")
    print(f"5 not in {lst1}  → {5 not in lst1}")
    print()

def main():
    print("\n=== Chapter 3: Operators Demo ===\n")
    demo_arithmetic()
    demo_comparison()
    demo_logical()
    demo_assignment()
    demo_precedence()
    demo_identity_membership()
    print("=== End of Chapter 3 ===\n")

if __name__ == "__main__":
    main()
