import sys

fst_line = sys.stdin.readline()
n = int(fst_line.split()[0])
k = int(fst_line.split()[1])
tmp_k = k
sec_line = sys.stdin.readline()
lst = list(map(int, sec_line.split()))
min_val = min(lst)
max_val = max(lst)
min_res = max_val - min_val
res = []
if min_res == 0:
    print(0, end=' ')
    print(0)
else:
    while k != 0 and min_res != 0:
        min_index = lst.index(min_val)
        max_index = lst.index(max_val)
        lst[min_index] += 1
        lst[max_index] -= 1
        min_val = min(lst)
        max_val = max(lst)
        res.append((max_index, min_index))
        k -= 1
        if max_val - min_val >= min_res:
            lst[min_index] -= 1
            lst[max_index] += 1
            k += 1
            res.pop()
            break
        min_res = max_val - min_val
    print(min_res, end=' ')
    print(tmp_k - k)
    for item in res:
        print(item[0]+1, end=' ')
        print(item[1]+1)
