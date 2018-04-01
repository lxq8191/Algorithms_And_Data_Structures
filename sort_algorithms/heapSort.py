heap_size = 0
LEFT = lambda i: 2*i+1
RIGHT = lambda i:2*i+2
#维护最大堆
def heapIfy(A,i):
    l, r = LEFT(i), RIGHT(i)
    largest = l if l < heap_size and A[l] > A[i] else i
    largest = r if r < heap_size and A[r] > A[largest] else largest
    if i!= largest:
        A[i], A[largest] = A[largest], A[i]
        heapIfy(A, largest)
#构建最大堆
def buildMaxHeap(A):
    global heap_size
    heap_size = len(A)
    for i in range(len(A)//2-1, -1, -1):
        heapIfy(A, i)
#堆排序
def heapSort(A):
    global heap_size
    buildMaxHeap(A)
    for i in range(len(A)-1, -1, -1):
        A[i], A[0] = A[0], A[i]
        heap_size -= 1
        heapIfy(A, 0)

a = [1,4,7,2,7,5,9,5]
print(heapSort(a))
print(a)
