#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
作者：Cyril
时间：2016年1月4号

希尔排序：
    插入排序的升级版，相隔为h的序列是有序的，然后不断缩小h。
知道h为1，这个最后一步就是插入操作。由于插入排序的性质，受输入
序列的顺序的影响。所以每一次插入排序都是在大部分是有序的序列上操
作的，所以速度很快。
"""


def shell_sorted(seq, comparator=cmp):
    count = len(seq)
    h = 1
    print count
    # 希尔间隔算子，貌似中不同值效果不一样，也有关于最优的选择，
    # 这里就不再讨论，有兴趣自行搜索
    while h < count / 3:
        h = h * 3 + 1
    # 这里是三层循环，其实内两层循环和插入排序基本上一模一样
    # 最外一层循环主要是取不同的间隔h，但最终间隔h＝1，最终使用插入排序
    while h >= 1:
        for i in range(h, count):
            for j in range(i, h - 1, -h):
                if comparator(seq[j], seq[j - h]) == -1:
                    seq[j], seq[j - h] = seq[j - h], seq[j]
        h /= 3  # 间隔不断缩短直到1

if __name__ == '__main__':
    array = [10, 4, 2, 5, 6, 1]
    shell_sorted(array)
    print array