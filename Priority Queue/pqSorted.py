#!/usr/bin/env python
# -*- coding:utf-8 -*-


def sink(array, k, n):
    while (2 * k + 1) < (n - 1):
        if array[2 * k] > array[k]:
            array[2 * k], array[k] = array[k], array[2 * k]
        elif array[2 * k + 1] > array[k]:
            array[2 * k + 1], array[k] = array[k], array[2 * k + 1]
        else:
            break


def pqSorted(array):
    n = len(array)
    for i in range(n / 2, 0, -1):
        sink(array, i, n)

    while n > 1:
        array[1], array[n - 1] = array[n - 1], array[1]
        n = n - 1
        sink(array, 1, n)


if __name__ == '__main__':
    array = [0, 2, 7, 3, 10, 89, 23, 67, 11]
    pqSorted(array)
    print array
