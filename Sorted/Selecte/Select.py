#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
作者：Cyril
时间：2016年1月3号

选择排序：
   首先，找到数组中的最小元素，然后和第一个元素交换位置
然后剩下的数组中再找到最小值和第二个数据交换，以此类推。
提供了自定义比较函数
"""


def select_sorted(seq, comparator=cmp):
    count = len(seq)
    for i in range(0, count):
        min_val = seq[i]
        min_index = i
        # 选择剩下的最小值
        for j in range(i + 1, count):
            if comparator(seq[j], min_val) < 0:
                min_val = seq[j]
                min_index = j
        # 交换
        seq[i], seq[min_index] = seq[min_index], seq[i]


if __name__ == '__main__':
    date = [8, 10, 5, 6, 1, 9]
    # 从大到小排序
    select_sorted(date, lambda x, y: cmp(y, x))
    print date
    # 默认从小到大排序
    select_sorted(date)
    print date
