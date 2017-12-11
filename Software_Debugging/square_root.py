import math
import random


def square_root(x, eps = 10e-7):
    assert x >= 0
    y = math.sqrt(x)
    assert abs(x - y * y) < eps
    return y


def main():
    for i in range(1, 1000):
        r = random.random() * 10000
        z = square_root(r)

    print 'Done!'


if __name__ == '__main__':
    main()
