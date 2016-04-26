#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def insert_sorted(sequence, comparator=cmp):
    count = len(sequence)
    x = np.arange(count)
    fig, axes = plt.subplots(ncols=1, nrows=count)
    axes_tuple = axes.ravel()
    axes_tuple[0].bar(x, np.array(sequence), 0.5)
    for i in range(1, count):
        # 将 array[j]插入到左边的有序数组中，丛右向左遍历
        for j in range(i, 0, -1):
            if comparator(sequence[j], sequence[j - 1]) < 0:
                # swap
                sequence[j], sequence[j - 1] = sequence[j - 1], sequence[j]
        axes_tuple[i].bar(x, np.array(sequence), 0.5)
    plt.show()


if __name__ == '__main__':
    array = np.random.randint(1, 200, (1, 6))[0]
    insert_sorted(list(array))
