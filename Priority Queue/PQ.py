#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MaxPQ(object):

    def __init__(self, compare=cmp):
        self.cmp = compare
        self.pq = [0, ]

    def swim(self, k):
        while (k > 1) and (self.cmp(self.pq[k], self.pq[k / 2]) > 0):
            self.pq[k], self.pq[k / 2] = self.pq[k / 2], self.pq[k]
            k = k / 2

    def insert(self, element):
        self.pq.append(element)
        print 'length of pq:' + str(len(self.pq))
        self.swim(len(self.pq) - 1)

    def getArray(self):
        return self.pq

    def sink(self, k):
        n = len(self.pq)
        while (k * 2 + 1) < (n - 1):
            if self.cmp(self.pq[k * 2], self.pq[k]):
                self.pq[k * 2], self.pq[k] = self.pq[k], self.pq[k * 2]
                k = k * 2
            elif self.cmp(self.pq[k * 2 + 1], self.pq[k]):
                self.pq[k * 2 + 1], self.pq[k] = self.pq[k], self.pq[k * 2 + 1]
                k = k * 2 + 1
            else:
                break

    def delMax(self):
        n = len(self.pq)
        self.pq[1] = self.pq[n - 1]
        self.pq.pop()
        self.sink(1)
if __name__ == '__main__':
    print 'Example ...'
    maxPQ = MaxPQ()
    maxPQ.insert(10)
    maxPQ.insert(20)
    maxPQ.insert(70)
    maxPQ.insert(40)
    maxPQ.insert(50)
    print maxPQ.getArray()
    maxPQ.delMax()
    print maxPQ.getArray()
    maxPQ.delMax()
    print maxPQ.getArray()
