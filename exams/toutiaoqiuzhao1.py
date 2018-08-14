import sys

fst_line = sys.stdin.readline()
m = int(fst_line)

lst = []
for i in range(m):
    line = sys.stdin.readline().strip().split(';')
    for item in line:
        tmp = item.split(',')
        lst.append((int(tmp[0]), int(tmp[1])))
lst = sorted(lst, key=lambda x:x[0])
res = []
low = lst[0][0]
high = lst[0][1]
for i in range(1,len(lst)):
    if lst[i][0] <= high:
        high = max(high, lst[i][1])
    else:
        res.append((low, high))
        low = lst[i][0]
        high = lst[i][1]
res.append((low, high))
# for i in range(len(lst)):
#     flag = 0
#     for j in range(len(res)):
#         before = lst[i]
#         after = res[j]
#         if not (after[0] > before[1] or after[1]< before[0]):
#             res[j] = (min(before[0], after[0]), max(before[1], after[1]))
#             flag = 1
#             break
#     if flag == 0:
#         res.append(lst[i])
for index in range(len(res) - 1):
    print(res[index][0], end=',')
    print(res[index][1], end=';')
print(res[len(res) - 1][0], end=',')
print(res[len(res) - 1][1])