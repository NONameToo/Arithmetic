# coding:utf-8

# 把后面无序的数据中的每一个和前面有序的数据中的元素作比较,放到合适的位置(操作有序这边)

# 最优时间复杂度: O(n)
# 最坏时间复杂度: O(n²)
# 稳定性: 稳定

def insert_sort(alist):
    """
    :param alist: 一个列表
    :j: 需要执行多少次排序
    :i: 需要进行排序的个数
    :return: 排序好的列表

    """
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break

    return alist


a = [1,5,4,2,7,4,9,6]
b = insert_sort(a)
print(b)

