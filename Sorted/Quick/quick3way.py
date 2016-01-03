#!/usr/bin/env python
# -*- coding-utf-8 -*-


def quickSorted(array, lo, hi, compare=cmp):
    if hi <= lo:
        return
    lt = lo
    i = lo + 1
    gt = hi
    v = array[lo]
    while i <= gt:
        cmpValue = compare(array[i], v)
        if cmpValue < 0:
            array[i], array[lt] = array[lt], array[i]
            i += 1
            lt += 1
        elif cmpValue > 0:
            array[i], array[gt] = array[gt], array[i]
            gt -= 1
        else:
            i += 1
    quickSorted(array, lo, lt - 1)
    quickSorted(array, gt + 1, hi)

if __name__ == '__main__':
    array = [1, 3, 2, 2, 9, 4, 4, 10, 6]
    quickSorted(array, 0, len(array) - 1)
    print array
