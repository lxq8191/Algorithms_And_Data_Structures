import sys

def perm(lst):
    if len(lst) <= 1:
        return [lst]
    res = []
    for i in range(len(lst)):
        s = lst[:i] + lst[i+1:]
        p = perm(s)
        for j in p:
            res.append(lst[i:i+1]+j)
    return res
 
fst_line = sys.stdin.readline()
n = int(fst_line)
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))
# print(perm(lst))
res = perm(lst)
result = []
for num in res:
    st = ''
    for i in range(len(num)):
        st += str(num[i])
    result.append(int(st))
result = sorted(result)
for num in result:
    print(num)
    # print('\n')
# print(result)