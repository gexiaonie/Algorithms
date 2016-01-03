# -*-coding:utf-8 -*-
'''
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
    #从大到小排序
    selectSorted(array,lambda x,y:cmp(y,x))
    print array
    #默认从小到大排序
    selectSorted(array)
    print array
