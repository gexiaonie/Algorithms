#!/usr/bin/env python
#! -*- coding:utf-8 -*-

import math


def merge(array, lo, mid, hi, compare=cmp):
    left = array[lo:mid]
    right = array[mid:hi + 1]
    leftLen = len(left)
    rightLen = len(right)
    indexOfLo = 0
    indexOfHi = 0
    for i in range(lo, hi + 1):
        if indexOfHi >= rightLen:
            array[i] = left[indexOfLo]
            indexOfLo += 1
        elif indexOfLo >= leftLen:
            array[i] = right[indexOfHi]
        elif compare(left[indexOfLo], right[indexOfHi]) == -1:
            array[i] = left[indexOfLo]
            indexOfLo += 1
        else:
            array[i] = right[indexOfHi]
            indexOfHi += 1


def min(number1, number2):
    if number1 > number2:
        return number2
    else:
        return number1


def mergeSorted(array):
    arrayLen = len(array)
    step = 1
    while step < arrayLen:
        lo = 0
        while lo < arrayLen - 1:
            hi = min(lo + step + step - 1, arrayLen - 1)
            mid = lo + step
            merge(array, lo, mid, hi)
            lo = hi + 1
        step = step * 2
if __name__ == '__main__':
    array = [10, 11, 12, 1, 2, 3]
    mergeSorted(array)
    print array
