"""This module provides some basic math functions.

该程序提供了一些基本的数学函数，包括加减乘除四则运算。

Example:
    >>> add(1, 2)
    3.0
    >>> subtract(1, 2)
    -1.0
    >>> multiply(1, 2)
    2.0
    >>> divide(1, 2)
    0.5
"""

from typing import TypeVar

T = TypeVar('T', int, float)


def add(a: T, b: T) -> float:
    """Add two numbers.

    Args:
        a (T): 第一个数
        b (T): 第二个数

    Returns:
        float: 两个数的和
    """
    return float(a + b)


def subtract(a: T, b: T) -> float:
    """Subtract two numbers.

    Args:
        a (T): 第一个数
        b (T): 第二个数

    Returns:
        float: 两个数的差
    """
    return float(a - b)


def multiply(a: T, b: T) -> float:
    """Multiply two numbers.

    Args:
        a (T): 第一个数
        b (T): 第二个数

    Returns:
        float: 两个数的积
    """
    return float(a * b)


def divide(a: T, b: T) -> float:
    """Divide two numbers.

    Args:
        a (T): 第一个数
        b (T): 第二个数

    Raises:
        ZeroDivisionError: 除数为0

    Returns:
        float: 两个数的商
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)

