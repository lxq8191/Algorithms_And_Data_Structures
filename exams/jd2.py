import sys 
def get_all(st):
    count = 0
    if len(st) == 1:
        return 1
    if st == st[::-1]:
        count += 1
    for gap in range(1,len(st)):
        temp = []
        for i in range(len(st)):
            if st[i:i+gap] not in temp:
                new_str = st[:i] + st[i+gap:]
                if new_str == new_str[::-1]:
                    count += 1
    return count

fst_line = sys.stdin.readline().strip('\n')
st = str(fst_line)
print(get_all(st))