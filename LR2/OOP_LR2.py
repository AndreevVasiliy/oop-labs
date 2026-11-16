"""Лабораторная работа 2. Matrix в ООП-стиле (операции через перегрузку операторов)."""
from typing import Sequence, Union

Number = Union[int, float]


class Matrix:
    def __init__(self, data: Sequence[Sequence[Number]]) -> None:
        rows = [list(row) for row in data]
        if not rows or not rows[0]:
            raise ValueError("matrix must not be empty")
        if any(len(row) != len(rows[0]) for row in rows):
            raise ValueError("all rows must have the same length")
        self._data: list[list[Number]] = rows

    @property
    def rows(self) -> int:
        return len(self._data)

    @property
    def cols(self) -> int:
        return len(self._data[0])

    def to_list(self) -> list[list[Number]]:
        return [row[:] for row in self._data]

    def __getitem__(self, index: tuple[int, int]) -> Number:
        i, j = index
        return self._data[i][j]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix):
            return NotImplemented
        return self._data == other._data

    def __repr__(self) -> str:
        return f"Matrix({self._data!r})"

    # ---------- операции ----------

    def __add__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            return NotImplemented
        if (self.rows, self.cols) != (other.rows, other.cols):
            raise ValueError("matrices must have the same shape")
        return Matrix(
            [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(self._data, other._data)]
        )

    def __mul__(self, other: Union["Matrix", Number]) -> "Matrix":
        # умножение на скаляр
        if isinstance(other, (int, float)):
            return Matrix([[a * other for a in row] for row in self._data])
        # умножение матриц
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("incompatible shapes for multiplication")
            other_cols = list(zip(*other._data))
            return Matrix(
                [[sum(a * b for a, b in zip(row, col)) for col in other_cols]
                 for row in self._data]
            )
        return NotImplemented

    def __rmul__(self, scalar: Number) -> "Matrix":
        """Позволяет писать 3 * m."""
        if isinstance(scalar, (int, float)):
            return self * scalar
        return NotImplemented

    def transpose(self) -> "Matrix":
        return Matrix([list(col) for col in zip(*self._data)])

    def determinant(self) -> Number:
        if self.rows != self.cols:
            raise ValueError("determinant is defined only for square matrices")
        return self._det(self._data)

    @staticmethod
    def _det(m: list[list[Number]]) -> Number:
        n = len(m)
        if n == 1:
            return m[0][0]
        if n == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        # разложение по первой строке
        total: Number = 0
        for j in range(n):
            minor = [row[:j] + row[j + 1:] for row in m[1:]]
            total += (-1) ** j * m[0][j] * Matrix._det(minor)
        return total


if __name__ == "__main__":
    m1 = Matrix([[1, 2], [2, 3]])
    m2 = Matrix([[2, 5], [7, 9]])

    m3 = m1 + m2
    m4 = m1 * m2
    m5 = m1.transpose()
    det = m1.determinant()

    assert m3 == Matrix([[3, 7], [9, 12]])
    assert m4 == Matrix([[16, 23], [25, 37]])
    assert m5 == Matrix([[1, 2], [2, 3]])
    assert det == -1
    assert m1 * 2 == 2 * m1 == Matrix([[2, 4], [4, 6]])
    assert Matrix([[1, 2, 3], [4, 5, 6]]).transpose() == Matrix([[1, 4], [2, 5], [3, 6]])
    assert Matrix([[2, 0, 1], [1, 3, 2], [1, 1, 4]]).determinant() == 18
    try:
        Matrix([[1, 2]]) + m1
    except ValueError:
        pass
    else:
        raise AssertionError("ожидался ValueError")
    print("lab2 oop: OK")
