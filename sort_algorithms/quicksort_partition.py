# coding=utf-8
# 给定一个数组，将该数组分成大于零和小于零的两部分
def qSort1(arr, low, high):
    if low < high:
        mid = Partition(arr, low, high)
        qSort1(arr, low, mid-1)
        qSort1(arr, mid+1, high)

#Partition
def Partition(arr, low, high):
    key = arr[0]
    while low < high:
        while low < high and arr[high] >= key:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= key:
            low += 1
        arr[high] = arr[low]
    arr[low] = key
    return low, arr



arr = [-4,5,-2,1,-8,6,7,7]
arr = [0] + arr 
Partition(arr, 0, len(arr)-1)
print(arr)