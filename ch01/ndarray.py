import numpy as np


def print_nd_1():
    # print(f'Hi, {name}')
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    b = np.array([10, 20, 30])
    print('a:\n', a)
    print('b:\n', b)
    print('a + b:\n', a + b)


def print_nd_2():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    print('a:\n', a)
    print('a.sum(axis=0):\n', a.sum(axis=0))
    print('a.sum(axis=1):\n', a.sum(axis=1))


if __name__ == '__main__':
    print_nd_1()
    print('\n==================================')
    print_nd_2()
