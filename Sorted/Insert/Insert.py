#!/usr/bin/env python
# -*- coding:utf-8 -*-


def insert_sorted(sequence, compare=cmp):

    """
    作者：Cyril
    时间：2016年1月3号

    插入排序：将数据分为两边，左边始终有序。每次插入要相应的移动左边数组。
    """

    count = len(sequence)
    for i in range(1, count):
        # 将 array[j]插入到左边的有序数组中，丛右向左遍历
        for j in range(i, 0, -1):
            if compare(sequence[j], sequence[j - 1]) < 0:
                # swap
                sequence[j], sequence[j - 1] = sequence[j - 1], sequence[j]


if __name__ == '__main__':
    array = [10, 2, 3, 5, 8, 6]
    insert_sorted(array)
    print array
