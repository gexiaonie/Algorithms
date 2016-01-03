# -*- coding:utf-8 -*-
'''
插入排序：
	将数据分为两边，左边
'''
def insertSorted(array,compare=cmp):
	count = len(array)
	for i in range(1,count):
		for j in range(i,0,-1):
			if compare(array[j], array[j - 1]) < 0:
				#swap
				array[j],array[j-1] = array[j-1],array[j]


if __name__ == '__main__':
	array = [10,2,3,5,8,6]
	insertSorted(array)
	print array