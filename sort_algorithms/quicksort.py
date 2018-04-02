# coding=utf-8
def quickSort(arr):
    less = []
    more = []
    pivotList = []
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    for i in range(len(arr)):
        if arr[i] < pivot:
            less.append(arr[i])
        elif arr[i] > pivot:
            more.append(arr[i])
        else:
            pivotList.append(arr[i])
    less = quickSort(less)
    more = quickSort(more)

    return less + pivotList + more

def qSort(arr):
    if not arr:
        return []
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        more = [j for j in arr[1:] if j >= pivot]
        less = qSort(less)
        more = qSort(more)
        return less + [pivot] + more

def qSort1(arr, low, high):
    if low < high:
        mid = getMid(arr, low, high)
        qSort1(arr, low, mid-1)
        qSort1(arr, mid+1, high)

#Partition
def getMid(arr, low, high):
    temp = arr[low]
    while low < high:
        while low < high and arr[high] >= temp:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= temp:
            low += 1
        arr[high] = arr[low]
    arr[low] = temp
    return low



arr = [4,5,2,1,8,6,7,7]
# print(quickSort(arr))
qSort1(arr, 0, len(arr)-1)
print(arr)