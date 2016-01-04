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

丛上图可以清楚看出来，该算法每次都是找到剩余的最小值和要找的第i小的值交换。对于长度为N的数组，选择排序需要大约N^2/2次比较和N交换。

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

丛上图可以查出，当第一遍历的时候，是将第二个元素和第一个元素进行比较。发现第二个元素（10）比第一个元素（23）小，交换他们的位置。第二次遍历的时候，将第三个元素（3）和第二个元素（23）比较，发现第三个元素（3）比第二个元素（23）小，交换位置。这个时候将第二个元素（发生改变了，变成3了）和第一个元素（10）比较，发现第二个元素（3）比第一个元素（10）小，将它们交换位置。以此类推，每次遍历都保证了左边的数据是有序的。直到遍历最后一个，整个数组就有序了。当输入数组是有序的时候，插入排序能够很快完成。所以插入排序能利用数组的初始特性。

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

# 希尔排序

希尔（Shell）排序是一种基于插入排序的快速排序算法。对于大规模乱序数组插入排序很慢，因为它只会交换相邻的元素，因此元素元素只能一点一点地从数组一端移动到另一端。希尔排序为了加速简单地改进了插入排序，交换不相邻的元素一对数组的局部进行排序，并最终用插入排序将局部有序的数组排序。

> 希尔排序的思想是使数组中任意间隔为h的相邻元素都是有序的。这样的数组被称为h有序数组。换句话说，一个h有序数组就是h个互相独立的有序数组编织在一起组成的一个数组。—— _<<算法>>(第四版)_

  2 | 1 | 4 | 0 | 6 | 3 | 11 | 5 | 10 | 9 |13 | 7
:--:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:--:
  2 |   |   |   | 6 |   |    |   | 10 |   |   |  
    | 1 |   |   |   | 3 |    |   |    | 9 |   |  
    |   | 4 |   |   |   | 11 |   |    |   | 13 |   
    |   |   | 0 |   |   |    | 5 |    |   |    | 7  

图 3. 一个h＝4有序数组即一个由h＝4个有序子数组组成的数组

``` python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
作者：Cyril
时间：2016年1月4号

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
    # 希尔间隔算子，貌似中不同值效果不一样，也有关于最优的选择，
    # 这里就不再讨论，有兴趣自行搜索
    while h < count / 3:
        h = h * 3 + 1
    # 这里是三层循环，其实内两层循环和插入排序基本上一模一样
    # 最外一层循环主要是取不同的间隔h，但最终间隔h＝1，最终使用插入排序
    while h >= 1:
        for i in range(h, count):
            for j in range(i, h - 1, -h):
                if compare(array[j], array[j - h]) == -1:
                    array[j], array[j - h] = array[j - h], array[j]
        h = h / 3  # 间隔不断缩短直到1

if __name__ == '__main__':
    array = [10, 4, 2, 5, 6, 1]
    shellSorted(array)
    print array
```

下面我们将采用柱状图的形式来跟踪插入排序算法的轨迹。主要是试用Python的[matplotlib](http://old.sebug.net/paper/books/scipydoc/matplotlib_intro.html)和[numpy](http://old.sebug.net/paper/books/scipydoc/numpy_intro.html)两个package。第一个包主要是类似于Matlab画图，第二个包类似于Matlab的矩阵操作（数值计算）。所有说Python是一门功能比较丰富的编程语言。

![希尔排序轨迹](shell.png)

``` python
# -*- coding:utf-8 -*-

'''
希尔排序：
	插入排序的升级版，相隔为h的序列是有序的，然后不断缩小h。
知道h为1，这个最后一步就是插入操作。由于插入排序的性质，受输入
序列的顺序的影响。所以每一次插入排序都是在大部分是有序的序列上操
作的，所以速度很快。
'''

import numpy as np
import matplotlib.pyplot as plt


def shellSorted(array):
    count = len(array)
    h = 1
    x = np.arange(count)
    rows = 1
    while h < count / 3:
        h = 3 * h + 1
        rows = rows + 1
    fig, axes = plt.subplots(ncols=1, nrows=rows + 1)
    axesTulpe = axes.ravel()
    index = 0
    axesTulpe[index].bar(x, np.array(array), 0.5)
    index += 1
    while h >= 1:
        # 插入排序，步进为h->1
        for i in range(h, count):
            for j in range(i, h - 1, -h):
                if array[j] < array[j - h]:
                    # swap
                    array[j - h], array[j] = array[j], array[j - h]
        axesTulpe[index].bar(x, np.array(array), 0.5)
        index += 1
        h = h / 3
    plt.show()

if __name__ == '__main__':
    array = np.random.randint(0, 200, (1, 100))[0]
    shellSorted(list(array))
```

# 冒泡排序

# 归并排序

# 快速排序

# 堆排序
