#!/usr/bin/env python
# -*- coding:utf-8 -*-


def sink(seq, k, n):
    while (2 * k + 1) < (n - 1):
        if seq[2 * k] > seq[k]:
            seq[2 * k], seq[k] = seq[k], seq[2 * k]
        elif seq[2 * k + 1] > seq[k]:
            seq[2 * k + 1], seq[k] = seq[k], seq[2 * k + 1]
        else:
            break


def pq_sorted(seq):
    n = len(seq)
    for i in range(n / 2, 0, -1):
        sink(seq, i, n)

    while n > 1:
        seq[1], seq[n - 1] = seq[n - 1], seq[1]
        n -= 1
        sink(seq, 1, n)


if __name__ == '__main__':
    array = [0, 2, 7, 3, 10, 89, 23, 67, 11]
    pq_sorted(array)
    print array
