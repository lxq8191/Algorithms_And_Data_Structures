# coding=utf-8
# 打印矩阵逆对角线
# 输入是n*n的方阵
def printMat(mat):
    n = len(mat)
    if n <= 0:
        return None
    if n == 1:
        print(mat)
    for i in range(n):
        print(mat[i][0], end=' ')
        temp = i
        for j in range(1,n):
            if temp  - 1 >= 0:
                print(mat[temp -1][j], end=' ')
                temp  = temp - 1
            else:
                break
    for k in range(1,n):
        print(mat[n-1][k], end=' ')
        temp = n - 1
        for m in range(k+1,n):
            if temp - 1 >= 0:
                print(mat[temp-1][m], end=' ')
                temp  = temp - 1
            else:
                break

m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
printMat(m)