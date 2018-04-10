import sys 
def get_x_and_y(lst):
    for cur in lst:
        if cur==2:
            print('1'+' '+'2')
        elif cur%2 != 0:
            print('No')
        else:
            res = []
            for x in range(1,cur):
                for y in range(1,cur):
                    if x % 2 !=0 and y % 2 == 0 and x * y == cur:
                        res.append(y)
            sorted(res)
            print(str(cur/res[0])+' '+str(res[0]))

fst_line = sys.stdin.readline()
n = int(fst_line)
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))
get_x_and_y(lst)