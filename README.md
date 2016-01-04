# Algorithms

# 概述

排序是将一组对象按照某种逻辑顺序重新排列的过程。而现在大部分编程语言都提供了排序算法，但是弄清楚排序算法还是有很多好处的。

* 通过对排序算法的分析有助于理解其他高深的算法
* 项目中遇到特定的排序问题，可以更具不同的应用场景选择不同的排序算法
* 很多面试题目里面也饱含了对排序算法的分析

整个算法的实现主要是参考 _<<算法>>(第四版)_ ，不过该书的算法实现主要是通过Java实现的。为了能达到学习的目的，我在这里将采用Python实现排序算法。不过后期可能考虑用其他语言编写，例如C/C++。

整个算法可以从我的[Github](https://github.com/Cyrilplus/Algorithms)中进行下载。

# 选择排序

> 一种最简单的排序算法是这样的：首先，找到数组中最小的元素，其次，将它和数组的第一个元素交换位置（例如第一个元素就是最小元素那么它就和它自己交换）。再次，在剩下的元素中找到最小的元素，将它与数组的第二个元素交换位置。如此往复，直到将整个数组排序。这种方法叫做选择排序，因为它在不断地选择剩余元素之中的最小者。—— _<<算法>>(第四版)_

i  | min | 10 | 3 | 7 | 1 | 2 | 9
:--:|:---:|:---:|:---:|:---:|:---:|:---:|:--:
0  | 1  | <font color="red">1</font> | 3  | 7  | <font color="red">10</font>  | 2  |  9
1  | 2  | 1  | <font color="red">2</font>  | 7  | 10  | <font color="red">3</font>  |  9
2  | 3  | 1  | 2  | <font color="red">3</font>  | 10  | <font color="red">7</font>  |  9
3  | 7  | 1  | 2  | 3  | <font color="red">7</font>  | <font color="red">10</font>  |  9
4  | 9  | 1  | 2  | 3  | 7  | <font color="red">9</font>  | <font color="red">10</font>

图 1. 选择排序轨迹

丛上图可以清楚看出来，该算法每次都是找到剩余的最小值和要找的第i小的值交换。对于长度为N的数组，选择排序需要大约$N^2/2$次比较和N交换。

``` python
#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
作者：Cyril
时间：2016年1月3号

选择排序：
	首先，找到数组中的最小元素，然后和第一个元素交换位置
然后剩下的数组中再找到最小值和第二个数据交换，以此类推。
提供了自定义比较函数
'''


def selectSorted(array, compare=cmp):
    count = len(array)
    for i in range(0, count):
        min = array[i]
        indexOfMin = i
        # 选择剩下的最小值
        for j in range(i + 1, count):
            if compare(array[j], min) < 0:
                min = array[j]
                indexOfMin = j
        # 交换
        array[i], array[indexOfMin] = array[indexOfMin], array[i]

if __name__ == '__main__':
    array = [8, 10, 5, 6, 1, 9]
    # 从大到小排序
    selectSorted(array, lambda x, y: cmp(y, x))
    print array
    # 默认从小到大排序
    selectSorted(array)
    print array
```

# 插入排序

> 通常人们整理桥牌的方法是一张一张的来，将每一张牌插入到其他已经有序的牌中的适当的位置。在计算机的实现中，为了给要插入的元素腾出空间，我们需要将其余所有元素在插入之前都向右移动一位。这种算法叫插入排序。—— _<<算法>>(第四版)_

i | 23 | 10 | 3 | 17 | 11 | 22 | 94
:--:|:---:|:---:|:---:|:---:|:---:|:---:|:--:
0 | <font color="red">10</font> | <font color="red">23</font> | 3 | 17 | 11 | 22 | 94  
1 | <font color="red">3</font> | 10 | <font color="red">23</font>  | 17  | 11  | 22  | 94  
2 | 3 | 10 | <font color="red">17</font> | <font color="red">23</font> | 11 | 22 | 94  
3 | 3 | 10 | <font color="red">11</font> | 17 | <font color="red">23</font> | 22 | 94  
4 | 3 | 10 | 11 | 17 | <font color="red">22</font> | <font color="red">23</font> | 94  
5 | 3 | 10 | 11 | 17 | 22 | <font color="red">23</font> | <font color="red">94</font>

图 2. 插入排序轨迹

丛上图可以查出，当第一遍历的时候，是将第二个元素和第一个元素进行比较。发现第二个元素（10）比第一个元素（23）小，交换他们的位置。第二次遍历的时候，将第三个元素（3）和第二个元素（23）比较，发现第三个元素（3）比第二个元素（23）小，交换位置。这个时候将第二个元素（发生改变了，变成3了）和第一个元素（10）比较，发现第二个元素（3）比第一个元素（10）小，将它们交换位置。以此类推，每次遍历都保证了左边的数据是有序的。直到遍历最后一个，整个数组就有序了。

``` python
# -*- coding:utf-8 -*-
'''
作者：Cyril
时间：2016年1月3号

插入排序：
	将数据分为两边，左边始终有序。每次插入要相应的移动左边数组。
'''


def insertSorted(array, compare=cmp):
    count = len(array)
    for i in range(1, count):
        # 将array[j]插入到左边的有序数组中，丛右向左遍历
        for j in range(i, 0, -1):
            if compare(array[j], array[j - 1]) < 0:
                # swap
                array[j], array[j - 1] = array[j - 1], array[j]


if __name__ == '__main__':
    array = [10, 2, 3, 5, 8, 6]
    insertSorted(array)
    print array
```

下面我们将采用柱状图的形式来跟踪插入排序算法的轨迹。主要是试用Python的matplotlib和numpy两个package。第一个包主要是类似于Matlab画图，第二个包类似于Matlab的矩阵操作（数值计算）。所有说Python是一门功能比较丰富的编程语言。
