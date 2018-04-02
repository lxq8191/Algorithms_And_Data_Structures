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
    
    print(low)
    print(high)

arr = [1,2,3,4,5,7]
value = 6
print(bSearch(arr, value))