# -*- coding:utf-8 -*-
class BinarySearch(object):
    """docstring for BinarySearch"""

    def rank(self, keyValue, source):
    	'二分查找法'
        lowIndex = 0
        highIndex = len(source) - 1
        while lowIndex <= highIndex:
            midIndex = (lowIndex + highIndex) / 2
            if keyValue < source[midIndex]:
                highIndex = midIndex - 1
            elif keyValue > source[midIndex]:
                lowIndex = midIndex + 1
            else:
                return midIndex
        return -1

if __name__ == '__main__':
    binarySearch = BinarySearch()
    data = [1, 5, 9, 2, 30, 8]
    sortedData = sorted(data)
    print sortedData
    print binarySearch.rank(9, sortedData)
    help(binarySearch.rank)
