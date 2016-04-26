#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
归并排序：
    递归归并排序。
"""

import numpy as np
import matplotlib.pyplot as plt


class Merge(object):
    """
    归并排序
    参数：
        array:是需要排序的数组
        compare:是比较函数，默认使用系统自带的cmp
    例子：
        array = [10 11 4 12 9 1]
        merge = Merge(array)
        merge.mergeSorted()
        array will be [1 4 9 10 11 12]

    """

    def __init__(self, sequence, compare=cmp):
        """
        归并排序
        参数：
            array:是需要排序的数组
            compare:是比较函数，默认使用系统自带的cmp
        """
        self.seq = sequence
        self.compare = compare
        self.merge_times = 0
        self.x = np.arange(len(sequence))
        fig, axes = plt.subplots(ncols=1, nrows=8)
        self.axes_tuple = axes.ravel()
        self.axes_tuple[self.merge_times].bar(self.x, np.array(sequence), 0.5)
        self.merge_times += 1

    def merge(self, lo, mid, hi):
        """
        归并插入：
            将array[lo...mid]和array[mid+1...hi](是有序的数组)，归并成一个有序的数组。
            并将结果存在原array数组里面
        参数：
            lo:是数组的低索引
            mid:是数组的中点
            hi：数组的高索引
        """
        lo_index = 0
        hi_index = 0
        left = self.seq[lo:mid + 1]
        right = self.seq[mid + 1:hi + 1]
        left_len = len(left)
        right_len = len(right)

        for i in range(lo, hi + 1):
            if lo_index >= left_len:
                self.seq[i] = right[hi_index]
                hi_index += 1
            elif hi_index >= right_len:
                array[i] = left[lo_index]
                lo_index += 1
            elif self.compare(left[lo_index], right[hi_index]) == -1:
                array[i] = left[lo_index]
                lo_index += 1
            else:
                array[i] = right[hi_index]
                hi_index += 1

    def sorted(self, lo, hi):
        """
        递归排序：
            使用中分治思想，递归知道需要将两个元素进行归并插入
        参数:
            lo:数组低索引
            hi:数组高索引
        """
        mid = int((lo + hi) / 2)
        if hi <= lo:
            return
        self.sorted(lo, mid)
        self.sorted(mid + 1, hi)
        self.merge(lo, mid, hi)
        if (hi - lo) > 24:
            self.axes_tuple[self.merge_times].bar(self.x, np.array(array), 0.5)
            self.merge_times += 1

    def merge_sorted(self):
        """
        归并排序：
            调用self.sorted函数，设置好数组的长度
        """
        self.sorted(0, len(self.seq) - 1)
        plt.show()

if __name__ == '__main__':
    array = list(np.random.randint(0, 200, (1, 200))[0])
    # print array
    merge = Merge(array)
    merge.merge_sorted()
    print merge.merge_times
    # print array
