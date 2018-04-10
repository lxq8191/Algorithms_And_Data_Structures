import sys 
def get_diff_num(lst, k):
    temp_lst = set([i+k for i in lst])
    return len(set(lst) & set(temp_lst))

fst_line = sys.stdin.readline()
n = int(fst_line.split()[0])
k = int(fst_line.split()[1])
line = sys.stdin.readline()
lst = list(map(int, line.split()))
print(get_diff_num(lst, k))