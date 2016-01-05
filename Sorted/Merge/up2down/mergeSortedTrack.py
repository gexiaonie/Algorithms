#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
归并排序：
    递归归并排序。
'''

import numpy as np
import matplotlib.pyplot as plt


class Merge(object):
    '''
    归并排序
    参数：
        array:是需要排序的数组
        compare:是比较函数，默认使用系统自带的cmp
    例子：
        array = [10 11 4 12 9 1]
        merge = Merge(array)
        merge.mergeSorted()
        array will be [1 4 9 10 11 12]

    '''

    def __init__(self, array, compare=cmp):
        '''
        归并排序
        参数：
            array:是需要排序的数组
            compare:是比较函数，默认使用系统自带的cmp
        '''
        self.array = array
        self.compare = compare
        self.mergeTimes = 0
        self.x = np.arange(len(array))
        fig, axes = plt.subplots(ncols=1, nrows=8)
        self.axesTulpe = axes.ravel()
        self.axesTulpe[self.mergeTimes].bar(self.x, np.array(array), 0.5)
        self.mergeTimes += 1

    def merge(self, lo, mid, hi):
        '''
        归并插入：
            将array[lo...mid]和array[mid+1...hi](是有序的数组)，归并成一个有序的数组。
            并将结果存在原array数组里面
        参数：
            lo:是数组的低索引
            mid:是数组的中点
            hi：数组的高索引
        '''
        indexOfLo = 0
        indexOfHi = 0
        left = self.array[lo:mid + 1]
        right = self.array[mid + 1:hi + 1]
        lenOfLeft = len(left)
        lenOfRight = len(right)

        for i in range(lo, hi + 1):
            if indexOfLo >= lenOfLeft:
                self.array[i] = right[indexOfHi]
                indexOfHi += 1
            elif indexOfHi >= lenOfRight:
                array[i] = left[indexOfLo]
                indexOfLo += 1
            elif self.compare(left[indexOfLo], right[indexOfHi]) == -1:
                array[i] = left[indexOfLo]
                indexOfLo += 1
            else:
                array[i] = right[indexOfHi]
                indexOfHi += 1

    def sorted(self, lo, hi):
        '''
        递归排序：
            使用中分治思想，递归知道需要将两个元素进行归并插入
        参数:
            lo:数组低索引
            hi:数组高索引
        '''
        mid = int((lo + hi) / 2)
        if hi <= lo:
            return
        self.sorted(lo, mid)
        self.sorted(mid + 1, hi)
        self.merge(lo, mid, hi)
        if (hi - lo) > 24:
            self.axesTulpe[self.mergeTimes].bar(self.x, np.array(array), 0.5)
            self.mergeTimes += 1

    def mergeSorted(self):
        '''
        归并排序：
            调用self.sorted函数，设置好数组的长度
        '''
        self.sorted(0, len(self.array) - 1)
        plt.show()

if __name__ == '__main__':
    array = list(np.random.randint(0, 200, (1, 200))[0])
    # print array
    merge = Merge(array)
    merge.mergeSorted()
    print merge.mergeTimes
    # print array
