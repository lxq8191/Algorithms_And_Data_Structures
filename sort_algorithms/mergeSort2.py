# coding=utf-8
# 使用归并排序的思想来统计数组中逆序数对的个数
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            global num
            num = num + len(left) - i #左边序列中剩余的数与当前right[j]构成逆序数对
            result.append(right[j])
            j += 1
    if i < len(left):
        result += left[i:]
    if j < len(right):
        result += right[j:]
    return result

num = 0
# a = [1,3,8,2,5,7,8]
a = [1, 7, 2, 9, 6, 4, 5, 3]
print(mergeSort(a))
print(num)