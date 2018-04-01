#二分查找
def bSearch(arr, value, low, high):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            return bSearch(arr, value, low, mid-1)
        elif arr[mid] < value:
            return bSearch(arr, value, mid+1, high)
    return -1

def bSearch2(arr, value):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            high = mid - 1
        elif arr[mid] < value:
            low = mid + 1
    return -1


arr = [1,2,3,4,5,6,7]
value = 6
print(bSearch(arr, value, 0, 6))
print(bSearch2(arr, value))
