import sys
def numParis(n, k):
    if k==0:
        return n*n
    res = 0
    for y in range(k+1,n+1):
        res += (n/y) * (y-k)
        if n % y >= k:
            res += (n/y) - k + 1
    return int(res)

fst_line = sys.stdin.readline()
n = int(fst_line.split()[0])
k = int(fst_line.split()[1])
print(numParis(n, k)) 