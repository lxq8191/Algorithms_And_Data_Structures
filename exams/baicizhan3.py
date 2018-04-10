import sys

def Test(lst):
    if len(lst)<=2:
        for j in range(len(lst)-1):
            print(str(lst[j])+',',end='')
        print(str(lst[len(lst)-1]))
    result = []
    start = 0
    end = 0
    while end < len(lst):
        if end+1 < len(lst) and lst[end+1] == lst[end] + 1:
            end += 1
        else:
            if start == end:
                result.append(str(lst[start]))
            elif (end - start)>=2:
                result.append(str(lst[start])+"-"+str(lst[end]))
            else:
                result.append(str(lst[start]))
                result.append(str(lst[start+1]))
            end += 1
            start = end
    for i in range(len(result)-1):
        print(result[i]+',', end='')
    print(result[len(result)-1])


fst_line = sys.stdin.readline()
n = int(fst_line)
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))
Test(lst)