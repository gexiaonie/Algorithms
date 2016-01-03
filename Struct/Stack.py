# -*- coding:utf-8 -*-

class Stack(object):
    """docstring for Stack"""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    items = [1, 2, 3, 4, 5]
    print items
    stack = Stack()
    for item in items:
        stack.push(item)
    print 'size : ' + str(stack.size())
    for i in range(0, 5):
        print stack.pop()
    print 'size : ' + str(stack.size())
