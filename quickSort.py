# coding:utf-8

# 快速排序的实现方法是设置两个游标，一个从前往后，一个从后往前，如果左侧游标所指数据大于右侧，
# 两数据进行交换，直到两个游标指向同一数据，则第一趟遍历结束。结束时游标所在数据，左侧都比其小
# 右侧都比其大,接下来对游标前后的两个序列进行递归操作。

# 最优时间复杂度: O(nlogn)
# 最坏时间复杂度: O(n²)
# 稳定性: 不稳定


def quick_sort(alist, first, last):
    """
    :param alist: 一个列表
    :param first: 起始位置
    :param last:  结束位置
    :return:      排序后的列表
    """

    if first >= last:
        return
    low = first
    high = last
    middle_value = alist[first]

    while low < high:
        while low < high and alist[high] >= middle_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < middle_value:
            low += 1
        alist[low] = alist[high]

    alist[low] = middle_value
    quick_sort(alist, low+1, last)
    quick_sort(alist, first, low-1)

    return alist
