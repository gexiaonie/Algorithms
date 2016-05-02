#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
作者: Cyril
冒泡排序：
    冒泡排序是最经典的排序之一，它重复地走访过要排序的数列，一次比较两个元素，
如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，
也就是说该数列已经排序完成。这个算法的名字由来是因为越大的元素会经由交换慢慢“浮”
到数列的顶端，故名冒泡排序。
"""


def bubble_sorted(sequence, comparator=cmp):
    count = len(sequence)
    for i in range(0, count - 1):
        for j in range(0, count - 1 - i):
            if comparator(sequence[j], sequence[j + 1]) > 0:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]


if __name__ == '__main__':
    array = [3, 4, 10, 1, 9, 5]
    bubble_sorted(array, lambda x, y: cmp(y, x))
    print array
    print help(bubble_sorted)
