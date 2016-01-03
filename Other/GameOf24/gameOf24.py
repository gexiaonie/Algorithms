#!/usr/bin/env python
# -*- coding:utf-8 -*-


import math

numbers = []


def isGet24(nCount):
    if nCount == 1:
        if math.fabs(24 - numbers[3]) < 1e-6:  # 防止浮点数计算误差
            return True
        else:
            return False
    for i in range(4 - nCount, 4):
        for j in range(i + 1, 4):
            a = numbers[i]
            b = numbers[j]
            numbers[j] = a + b
            if isGet24(nCount - 1) == True:
                return True
            numbers[j] = a - b
            if isGet24(nCount - 1) == True:
                return True
            numbers[j] = b - a
            if isGet24(nCount - 1) == True:
                return True
            numbers[j] = a * b
            if isGet24(nCount - 1) == True:
                return True
            if b != 0:
                numbers[j] = float(a) / b
                if isGet24(nCount - 1) == True:
                    return True
            if a != 0:
                numbers[j] = float(b) / a
                if isGet24(nCount - 1) == True:
                    return True
            numbers[i] = a
            numbers[j] = b
    return False

if __name__ == '__main__':
    numbers = []
    for i in range(1, 5):
        number = raw_input('input number%d:' % i)
        numbers.append(int(number))
    result = isGet24(4)
    print result
