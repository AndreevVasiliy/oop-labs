"""Лабораторная работа 1. Stack и Queue в ООП-стиле."""
from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """Стек (LIFO)."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items!r})"


class Queue(Generic[T]):
    """Очередь (FIFO). Внутри deque, чтобы dequeue был O(1)."""

    def __init__(self) -> None:
        self._items: deque[T] = deque()

    def enqueue(self, item: T) -> None:
        self._items.append(item)

    def dequeue(self) -> T:
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self) -> T:
        if not self._items:
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Queue({list(self._items)!r})"


if __name__ == "__main__":
    s: Stack[int] = Stack()
    for x in (1, 2, 3):
        s.push(x)
    assert s.peek() == 3 and len(s) == 3
    assert [s.pop(), s.pop(), s.pop()] == [3, 2, 1]
    assert s.is_empty()

    q: Queue[str] = Queue()
    for w in ("a", "b", "c"):
        q.enqueue(w)
    assert q.peek() == "a" and len(q) == 3
    assert [q.dequeue(), q.dequeue(), q.dequeue()] == ["a", "b", "c"]
    assert q.is_empty()

    try:
        s.pop()
    except IndexError:
        pass
    else:
        raise AssertionError("ожидался IndexError")
    print("lab1 oop: OK")
