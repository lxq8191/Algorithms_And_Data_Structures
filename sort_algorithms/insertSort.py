def insertSort(arr):
    if len(arr) <= 1:
        return arr
    # 从第一个元素开始
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

a = [1,7,4,9,3]
print(insertSort(a))