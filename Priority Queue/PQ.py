#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MaxPQ(object):
    def __init__(self, compare=cmp):
        self.cmp = compare
        self.pq = [0, ]
        self.N = 0

    def swim(self, k):
        while (k > 1) and (self.cmp(self.pq[k], self.pq[k / 2]) > 0):
            self.pq[k], self.pq[k / 2] = self.pq[k / 2], self.pq[k]
            k /= 2

    def insert(self, element):
        self.pq.append(element)
        self.N += 1
        self.swim(self.N)

    def get_array(self):
        return self.pq

    def sink(self, k):
        while (k * 2) <= self.N:
            j = 2 * k
            if j < self.N:
                if self.cmp(self.pq[j + 1], self.pq[j]) > 0:
                    j += 1
            if self.cmp(self.pq[j], self.pq[k]) > 0:
                self.pq[j], self.pq[k] = self.pq[k], self.pq[j]
                k = j
            else:
                break

    def del_max(self):
        max_val = self.pq[1]
        self.pq[1], self.pq[self.N] = self.pq[self.N], self.pq[1]
        self.N -= 1
        self.sink(1)
        return max_val


if __name__ == '__main__':
    print 'Example ...'
    max_pq = MaxPQ()
    max_pq.insert(10)
    max_pq.insert(20)
    max_pq.insert(70)
    max_pq.insert(40)
    max_pq.insert(50)
    print max_pq.N
    print max_pq.get_array()
    print max_pq.del_max()
    print max_pq.del_max()
    print max_pq.del_max()
    print max_pq.del_max()
    print max_pq.del_max()
    print max_pq.get_array()
