# src/chapter17.py

"""
Chapter 17 – Type Hints & Static Typing
Author: Luca Bocaletto
Description:
    Demonstrate Python type annotations for functions, variables,
    use of typing module (List, Dict, Optional, Union, Any),
    generics with TypeVar & Generic, and introspection of __annotations__.
"""

from typing import List, Dict, Optional, Union, Any, TypeVar, Generic

# 1. Function Annotations
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

# 2. Variable Annotations
ages: List[int] = [25, 30, 35]
threshold: float = 4.5

# 3. Common typing constructs
def find_user(user_id: int) -> Optional[Dict[str, Any]]:
    users = {
        1: {"name": "Alice", "roles": ["admin"]},
        2: {"name": "Bob",   "roles": ["user"]}
    }
    return users.get(user_id)

def process(data: Union[str, bytes]) -> None:
    if isinstance(data, bytes):
        print(data.decode('utf-8'))
    else:
        print(data)

# 4. Generics & TypeVar
T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

# Demo functions
def demo_function_annotations():
    print("== Function Annotations Demo ==")
    print("greet.__annotations__:", greet.__annotations__)
    print("add.__annotations__:", add.__annotations__)
    print()

def demo_variable_annotations():
    print("== Variable Annotations Demo ==")
    print("Global __annotations__ dict:", globals().get('__annotations__'))
    print()

def demo_typing_module():
    print("== typing Module Demo ==")
    user = find_user(2)
    print("find_user(2) →", user)
    missing = find_user(99)
    print("find_user(99) →", missing)
    print("process('hello world') →", end=" ")
    process("hello world")
    print("process(b'bytes here') →", end=" ")
    process(b"bytes here")
    print()

def demo_generics():
    print("== Generics & Stack Demo ==")
    int_stack = Stack[int]()
    str_stack = Stack[str]()
    for i in (1, 2, 3):
        int_stack.push(i)
    for s in ("a", "b", "c"):
        str_stack.push(s)
    print("int_stack.pop():", int_stack.pop())
    print("str_stack.pop():", str_stack.pop())
    print()

def main():
    print("\n=== Chapter 17: Type Hints & Static Typing Demo ===\n")
    demo_function_annotations()
    demo_variable_annotations()
    demo_typing_module()
    demo_generics()
    print("=== End of Chapter 17 ===\n")

if __name__ == "__main__":
    main()
