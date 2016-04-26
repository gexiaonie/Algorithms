#!/usr/bin/env python
# -*- coding-utf-8 -*-


def quick_sorted(seq, lo, hi, compare=cmp):
    if hi <= lo:
        return
    lt = lo
    i = lo + 1
    gt = hi
    v = seq[lo]
    while i <= gt:
        cmp_value = compare(seq[i], v)
        if cmp_value < 0:
            seq[i], seq[lt] = seq[lt], seq[i]
            i += 1
            lt += 1
        elif cmp_value > 0:
            seq[i], seq[gt] = seq[gt], seq[i]
            gt -= 1
        else:
            i += 1
    quick_sorted(seq, lo, lt - 1)
    quick_sorted(seq, gt + 1, hi)

if __name__ == '__main__':
    array = [1, 3, 2, 2, 9, 4, 4, 10, 6]
    quick_sorted(array, 0, len(array) - 1)
    print array
