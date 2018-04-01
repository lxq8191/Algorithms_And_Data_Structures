def bubbleSort(arr):
    if len(arr) == 0:
        return arr
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i] # python独特的交换方式
    return arr

def bubbleSort2(arr):
    if len(arr) == 0:
        return arr
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

a3 = [1,3,4,2,1]
print(bubbleSort2(a3))