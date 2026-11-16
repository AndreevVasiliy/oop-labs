"""Лабораторная работа 1. Stack и Queue в функциональном стиле.

Структуры данных - обычные списки, операции - чистые функции:
они не меняют переданный объект, а возвращают новый.
"""
from typing import TypeVar

T = TypeVar("T")

Stack = list[T]
Queue = list[T]


# ---------- Stack ----------

def stack_new() -> Stack[T]:
    return []


def stack_push(stack: Stack[T], item: T) -> Stack[T]:
    return [*stack, item]


def stack_pop(stack: Stack[T]) -> tuple[T, Stack[T]]:
    """Возвращает (извлечённый элемент, новый стек)."""
    if not stack:
        raise IndexError("pop from empty stack")
    return stack[-1], stack[:-1]


def stack_peek(stack: Stack[T]) -> T:
    if not stack:
        raise IndexError("peek from empty stack")
    return stack[-1]


def stack_is_empty(stack: Stack[T]) -> bool:
    return not stack


def stack_size(stack: Stack[T]) -> int:
    return len(stack)


# ---------- Queue ----------

def queue_new() -> Queue[T]:
    return []


def queue_enqueue(queue: Queue[T], item: T) -> Queue[T]:
    return [*queue, item]


def queue_dequeue(queue: Queue[T]) -> tuple[T, Queue[T]]:
    """Возвращает (извлечённый элемент, новая очередь)."""
    if not queue:
        raise IndexError("dequeue from empty queue")
    return queue[0], queue[1:]


def queue_peek(queue: Queue[T]) -> T:
    if not queue:
        raise IndexError("peek from empty queue")
    return queue[0]


def queue_is_empty(queue: Queue[T]) -> bool:
    return not queue


def queue_size(queue: Queue[T]) -> int:
    return len(queue)


if __name__ == "__main__":
    s0: Stack[int] = stack_new()
    s1 = stack_push(stack_push(stack_push(s0, 1), 2), 3)
    assert s0 == [] and s1 == [1, 2, 3]  # исходные данные не изменились
    top, s2 = stack_pop(s1)
    assert top == 3 and s2 == [1, 2] and s1 == [1, 2, 3]
    assert stack_peek(s2) == 2 and stack_size(s2) == 2

    q0: Queue[str] = queue_new()
    q1 = queue_enqueue(queue_enqueue(q0, "a"), "b")
    head, q2 = queue_dequeue(q1)
    assert head == "a" and q2 == ["b"] and q1 == ["a", "b"]
    assert queue_is_empty(queue_new()) and not queue_is_empty(q2)

    try:
        stack_pop(stack_new())
    except IndexError:
        pass
    else:
        raise AssertionError("ожидался IndexError")
    print("lab1 functional: OK")
