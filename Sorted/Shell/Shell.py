# -*- coding:utf-8 -*-

'''
希尔排序：
	插入排序的升级版，相隔为h的序列是有序的，然后不断缩小h。
知道h为1，这个最后一步就是插入操作。由于插入排序的性质，受输入
序列的顺序的影响。所以每一次插入排序都是在大部分是有序的序列上操
作的，所以速度很快。
'''


def shellSorted(array, compare=cmp):
    count = len(array)
    h = 1
    print count
    while h < count / 3:
        h = h * 3 + 1
    while h >= 1:
        for i in range(h, count):
            for j in range(i, h - 1, -h):
                if compare(array[j], array[j - h]) == -1:
                    array[j], array[j - h] = array[j - h], array[j]
        h = h / 3

if __name__ == '__main__':
    array = [10, 4, 2, 5, 6, 1]
    shellSorted(array)
    print array
