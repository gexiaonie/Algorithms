# -*- coding:utf-8 -*-


def rank(key, source):

    """
    :param key: find key from source
    :param source: find key from source
    :return: index of source. if key is not in source , return -1
    """

    low_index = 0
    high_index = len(source) - 1
    while low_index <= high_index:
        mid_index = (low_index + high_index) / 2
        if key < source[mid_index]:
            high_index = mid_index - 1
        elif key > source[mid_index]:
            low_index = mid_index + 1
        else:
            return mid_index
    return -1


if __name__ == '__main__':
    data = [1, 5, 9, 2, 30, 8]
    sortedData = sorted(data)
    print sortedData
    print rank(9, sortedData)
    help(rank)
