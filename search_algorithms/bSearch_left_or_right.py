# coding=utf-8
# 二分查找与target相等的最左边的值
def bSearch_left(lst, target):
    if len(lst) <= 0:
        return lst
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            while lst[mid] == target:
                mid = mid - 1
            return mid + 1
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 二分查找与target相等的最右边的值
def bSearch_right(lst, target):
    if len(lst) <= 0:
        return lst
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            while lst[mid] == target:
                mid = mid + 1
            return mid - 1
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1,2,6,7,8,9]
target = 6
print(bSearch_left(arr, target))
print(bSearch_right(arr, target))