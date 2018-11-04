# coding:utf-8


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



a = [1,5,4,2,7,4,9,6]
b = quick_sort(a, 0, len(a)-1)
print(b)







