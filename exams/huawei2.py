#coding=utf-8
import sys 

def longIntMul(numA,numB):
    numA.reverse()
    numB.reverse()

    result = [0 for i in range(0,len(numA)+len(numB))]
    for i in range(len(numA)):
        for j in range(len(numB)):
            result += numA[i]*numB[j]
    for k in range(len(result)):
        if result[k] > 9:
            result[k+1] += result[k]/10
            result[k] = result[k] % 10
    result.reverse()
    print('hhhh')
    return result

if __name__ == "__main__":
    inputs = []
    j = 0
    for line in sys.stdin:
        if j > 1:
            break
        inputs.append(line)
        j += 1
    lstA = list(inputs[0])
    lstB = list(inputs[1])
    flagA = True
    flagB = True
    if lstA[0] == '-':
        flagA = False
        del lstA[0]
    if lstA[0] == '-':
        flagB = False
        del lstA[0]
    for i in range(len(lstA)):
        lstA[i] = int(lstA[i])
    for j in range(len(lstB)):
        lstB[j] = int(lstB[j])
        # a = line.split()
    if not (flagA ^ flagB):
        print(longIntMul(lstA,lstB))
    else:
        print(-longIntMul(lstA,lstB))
# line = input()
# findMaxIntString(line)