def selectSort(arr):
    if len(arr) <= 1:
        return arr
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

a = [1,7,4,9,3,0]
print(selectSort(a))