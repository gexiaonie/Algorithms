#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
归并排序：
    待续。。。
'''


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
        indexOfLo = lo
        indexOfHi = mid + 1
        copyArray = self.array[lo:hi]
        for i in range(lo, hi + 1):
            if indexOfLo > mid:
                self.array[i] = copyArray[indexOfHi]
                indexOfHi += 1
            elif indexOfHi > hi:
                array[i] = copyArray[indexOfLo]
                indexOfLo += 1
            elif self.compare(copyArray[indexOfLo], copyArray[indexOfHi]) == -1:
                array[i] = copyArray[indexOfLo]
                indexOfLo += 1
            else:
                array[i] = copyArray[indexOfHi]
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

    def mergeSorted(self):
        '''
        归并排序：
            调用self.sorted函数，设置好数组的长度
        '''
        self.sorted(0, len(self.array) - 1)

if __name__ == '__main__':
    array = [10, 11, 12, 0, 1, 2, 100, 89, 47]
    merge = Merge(array)
    merge.mergeSorted()
    print array
    print merge.sorted.__doc__
    print __doc__
