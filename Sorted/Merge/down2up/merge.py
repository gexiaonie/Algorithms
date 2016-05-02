#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
作者：Cyril
时间：2016年1月5号
归并排序：
    非递归归并排序。
"""


def merge(sequence, lo, mid, hi, compare=cmp):
    left = sequence[lo:mid]
    right = sequence[mid:hi + 1]
    left_len = len(left)
    right_len = len(right)
    index_lo = 0
    index_hi = 0
    for i in range(lo, hi + 1):
        if index_hi >= right_len:
            sequence[i] = left[index_lo]
            index_lo += 1
        elif index_lo >= left_len:
            sequence[i] = right[index_hi]
        elif compare(left[index_lo], right[index_hi]) == -1:
            sequence[i] = left[index_lo]
            index_lo += 1
        else:
            sequence[i] = right[index_hi]
            index_hi += 1


def merge_sorted(sequence):
    length = len(sequence)
    step = 1
    while step < length:
        lo = 0
        while lo < length - 1:
            hi = min(lo + step + step - 1, length - 1)
            mid = lo + step
            merge(sequence, lo, mid, hi)
            lo = hi + 1
        step *= 2


if __name__ == '__main__':
    array = [10, 11, 12, 1, 2, 3]
    merge_sorted(array)
    print array
