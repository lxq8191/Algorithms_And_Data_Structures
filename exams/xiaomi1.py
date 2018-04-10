# 从给定的有序列表中查找出一个与目标值相差（绝对值）最小的值
def bSearch(lst, val):
    minDist = val
    low = 0
    high = len(lst) - 1
    # if val in lst:
    #     return val
    while low < high:
        mid = (low + high) // 2
        if minDist > abs(lst[mid] - val):
            minDist = abs(lst[mid] - val) 
        front = abs(lst[mid-1] - val) 
        back = abs(lst[mid+1] - val)
        if minDist == 0:
            return lst[mid]
        elif front > minDist and back > minDist:
            return lst[mid]
        elif front <= minDist and back > minDist:
            high = mid - 1
            minDist = front
        elif front > minDist and back <= minDist:
            low = mid + 1
            minDist = back
        elif front <= back:
            high = mid - 1
            minDist = front
        elif front > back:
            low = mid + 1
            minDist = back
        print(minDist)
    return -1

def bSearch2(arr, value):
    low = 0
    high = len(arr) - 1
    if value <= arr[0]:
        return 0
    elif value >= arr[len(arr) - 1]:
        return len(arr) - 1 
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            high = mid - 1
        elif arr[mid] < value:
            low = mid + 1
    index = low
    minDist = abs(arr[low] - val)
    if low - 1 >=0 and minDist > abs(arr[low-1] - val):
        minDist = abs(arr[low-1] - val)
        index = low - 1
    elif low + 1 <= (len(arr)-1) and minDist > abs(arr[low+1] - val):
        minDist = abs(arr[low+1] - val)
        index = low + 1
    return index

def bSearch3(arr, value):
    low = 0
    high = len(arr) - 1
    if value <= arr[0]:
        return 0
    elif value >= arr[len(arr) - 1]:
        return len(arr) - 1 
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            high = mid - 1
        elif arr[mid] < value:
            low = mid + 1
    if abs(arr[low] - val) > abs(arr[high] - val):
        return arr[high]
    else:
        return arr[low]

# lst = [1,4,7,8,8,8,8,8,8,8,8,8,9,10,13,16]
lst = [2,5,7,20,32,89,120,123,500]
val = 33
print(bSearch3(lst, val))