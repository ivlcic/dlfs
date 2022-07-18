import numpy as np
from numpy import ndarray
from typing import Callable
from plot import plot_single


def square(x: ndarray) -> ndarray:
    return np.power(x, 2)


def leaky_relu(x: ndarray) -> ndarray:
    return np.maximum(0.2 * x, x)


def sigmoid(x: ndarray) -> ndarray:
    return 1 / (1 + np.exp(-x))


def deriv(func: Callable[[ndarray], ndarray], x: ndarray, delta: float = 0.001) -> ndarray:
    return (func(x + delta) - func(x - delta)) / (2 * delta)


def print_deriv_1():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    print('a:\n', a)
    print('deriv(square, a):\n', deriv(square, a))
    print('deriv(leaky_relu, a):\n', deriv(leaky_relu, a))


if __name__ == '__main__':
    print_deriv_1()
    print('\n==================================')
    input_range = np.arange(-2, 2, 0.01)
    plot_single([
        input_range, square(input_range),
        input_range, leaky_relu(input_range)
    ], [
        'Square function',
        '"ReLU" function'
    ])
