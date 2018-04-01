def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while (i - gap) >= 0:
                if arr[i] < arr[i - gap]:
                    arr[i], arr[i - gap] = arr[i - gap], arr[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return arr

a = [1,5,7,4,3]
print('原列表= %s' % a)
print('原列表= %s, 新列表= %s' % (a, shellSort(a)))