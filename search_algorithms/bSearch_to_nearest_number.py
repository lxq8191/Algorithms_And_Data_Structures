def bSearch(lst, val):
    low = 0
    high = len(lst) - 1
    while low < high:
        mid = (low + high) // 2
        if lst[mid] == val:
            return mid
        if low < high and lst[mid] < val:
            low = mid + 1
        if low < high and lst[mid] > val:
            high = mid - 1
    
    if low - 1 > 0 and abs(lst[low-1] - val) < abs(lst[low] - val):
        return low - 1
    elif high + 1 < len(lst) and abs(lst[high + 1] - val) < abs(lst[high] - val):
        return high + 1
    else:
        return low

arr = [1,2,3,4,7,7,9]
value = 6
print(bSearch(arr, value))