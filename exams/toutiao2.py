import sys 
def get_magic_num(lst_a, lst_b):
    if len(lst_a) <= 1:
        return 0
    a_mean = sum(lst_a)/len(lst_a)
    b_mean = sum(lst_b)/len(lst_b)
    # print([i for i in lst_a if i <=a_mean and i>=b_mean and i not in lst_b])
    num = len([i for i in lst_a if i <=a_mean and i>=b_mean and i not in lst_b])
    return num

fst_line = sys.stdin.readline()
n = int(fst_line.split()[0])
m = int(fst_line.split()[1])
sec_line = sys.stdin.readline()
lst_a = list(map(int, sec_line.split()))
third_line = sys.stdin.readline()
lst_b = list(map(int, third_line.split()))
sorted(lst_a)
sorted(lst_b)
# print(lst_a)
# print(lst_b)
print(get_magic_num(lst_a, lst_b) + get_magic_num(lst_b, lst_a))
