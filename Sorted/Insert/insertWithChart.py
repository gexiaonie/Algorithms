#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def insertSorted(array, compare=cmp):
    count = len(array)
    x = np.arange(count)
    fig, axes = plt.subplots(ncols=1, nrows=count)
    axesTulpe = axes.ravel()
    axesTulpe[0].bar(x, np.array(array), 0.5)
    for i in range(1, count):
        # 将 array[j]插入到左边的有序数组中，丛右向左遍历
        for j in range(i, 0, -1):
            if compare(array[j], array[j - 1]) < 0:
                # swap
                array[j], array[j - 1] = array[j - 1], array[j]
        axesTulpe[i].bar(x, np.array(array), 0.5)
    plt.show()

if __name__ == '__main__':
    array = np.random.randint(1, 200, (1, 6))[0]
    insertSorted(list(array))
