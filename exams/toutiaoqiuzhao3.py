import sys

fst_line = sys.stdin.readline()
n = int(fst_line)
lst = []
sum = 0
for i in range(n):
    line = sys.stdin.readline().strip().split()
    a = int(line[0])
    b = int(line[1])
    sum += b
print(sum)