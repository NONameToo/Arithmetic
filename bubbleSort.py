# coding:utf-8

# 比较相邻的元素,大的往后走

# 最优时间复杂度: O(n)
# 最坏时间复杂度: O(n²)
# 稳定性: 稳定


def bubble_sort(alist):
    """

    :param alist: 一个列表
    :param j: 外层循环表示要走多少回
    :param i: 内层循环表示每回走要比较多少次数据
    :return: 排序好之后的列表
    """
    n = len(alist)
    for j in range(n-1):
        for i in range(n-j-1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist


a = [1,5,4,2,7,4,9,6]
b = bubble_sort(a)
print(b)





