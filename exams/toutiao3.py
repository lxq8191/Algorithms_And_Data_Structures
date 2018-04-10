import sys 
def get_max_num(N, K, H, lst):
    high = 0
    start = 0
    sorted(lst, reverse=True)
    for i in lst:
        if abs(i-start) <= H and K > 0:
            temp = high
            high = start + (i - start)*2
            if high < 0:
                high = temp
                del i
            else:
                start = high
                K -= 1
                del i        
    return high
    
fst_line = sys.stdin.readline()
n = int(fst_line.split()[0])
k = int(fst_line.split()[1])
h = int(fst_line.split()[2])
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))
print(get_max_num(n, k, h, lst))
