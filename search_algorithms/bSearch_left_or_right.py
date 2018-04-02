# coding=utf-8
# 二分查找与target相等的最左边的值
def bSearch_left(lst, target):
    if len(lst) <= 0:
        return lst
    left = 0
    right = len(lst) - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] > target:
            left = mid + 1
        else:
            right = mid
    if lst[right] == target:
        return right
    return -1

# 二分查找与target相等的最右边的值
def bSearch_right(lst, target):
    if len(lst) <= 0:
        return lst
    left = 0
    right = len(lst) - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] >= target:
            left = mid
        else:
            right = mid - 1
    if lst[left] == target:
        return left
    return -1