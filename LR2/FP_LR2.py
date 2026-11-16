"""Лабораторная работа 2. Матрицы в функциональном стиле.

Матрица - обычный список списков, операции - чистые функции.
"""
from typing import Union

Number = Union[int, float]
MatrixData = list[list[Number]]


def matrix_new(data: MatrixData) -> MatrixData:
    """Проверяет данные и возвращает копию."""
    if not data or not data[0]:
        raise ValueError("matrix must not be empty")
    if any(len(row) != len(data[0]) for row in data):
        raise ValueError("all rows must have the same length")
    return [row[:] for row in data]


def shape(m: MatrixData) -> tuple[int, int]:
    return len(m), len(m[0])


def add(a: MatrixData, b: MatrixData) -> MatrixData:
    if shape(a) != shape(b):
        raise ValueError("matrices must have the same shape")
    return [[x + y for x, y in zip(r1, r2)] for r1, r2 in zip(a, b)]


def multiply(a: MatrixData, b: MatrixData) -> MatrixData:
    if shape(a)[1] != shape(b)[0]:
        raise ValueError("incompatible shapes for multiplication")
    b_cols = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in b_cols] for row in a]


def scalar_multiply(m: MatrixData, scalar: Number) -> MatrixData:
    return [[x * scalar for x in row] for row in m]


def transpose(m: MatrixData) -> MatrixData:
    return [list(col) for col in zip(*m)]


def determinant(m: MatrixData) -> Number:
    rows, cols = shape(m)
    if rows != cols:
        raise ValueError("determinant is defined only for square matrices")
    if rows == 1:
        return m[0][0]
    if rows == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    # разложение по первой строке
    total: Number = 0
    for j in range(cols):
        minor = [row[:j] + row[j + 1:] for row in m[1:]]
        total += (-1) ** j * m[0][j] * determinant(minor)
    return total


if __name__ == "__main__":
    m1 = matrix_new([[1, 2], [2, 3]])
    m2 = matrix_new([[2, 5], [7, 9]])

    m3 = add(m1, m2)
    m4 = multiply(m1, m2)
    m5 = transpose(m1)
    det = determinant(m1)

    assert m3 == [[3, 7], [9, 12]]
    assert m4 == [[16, 23], [25, 37]]
    assert m5 == [[1, 2], [2, 3]]
    assert det == -1
    assert scalar_multiply(m1, 2) == [[2, 4], [4, 6]]
    assert m1 == [[1, 2], [2, 3]]  # исходные данные не изменились
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert determinant([[2, 0, 1], [1, 3, 2], [1, 1, 4]]) == 18
    print("lab2 functional: OK")
