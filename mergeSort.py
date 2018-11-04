# coding:utf-8

# 归并排序就是先递归分散数组,再合并数组
# 最优时间复杂度: O(nlogn)
# 最坏时间复杂度: O(nlogn)
# 稳定性: 稳定


def merge_sort(alist):
    """
    :param alist: 一个列表
    :return: 排序好的列表
    :left_pointer: 左边列表的游标
    :right_pointer:  右边列表的游标
    """
    n = len(alist)
    if n <= 1:
        return alist

    mid = n//2
    left_li = merge_sort(alist[: mid])
    right_li = merge_sort(alist[mid:])
    result = []

    left_pointer, right_pointer = 0, 0
    while left_pointer < len(left_li) and right_pointer < len(right_li):

        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1

        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result

a = [1,5,4,2,7,4,9,6]
b = merge_sort(a)
print(b)
