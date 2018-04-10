#coding=utf-8

def findMaxIntString(st):
    if len(st) <= 0:
        return ''
    maxInt = 0
    res = []

    i = 0
    while i < len(st):
        if st[i].isdigit():
            temp = st[i]
            index_num = 1
            while i + index_num < len(st) and st[i+index_num].isdigit():
                temp += st[i+index_num]
                index_num += 1
            res.append(temp)
            if int(temp) > maxInt:
                maxInt = int(temp)
            i += index_num
        else:
            i += 1
    # print(res)
    # for j in range(len(res)-1,-1,-1):
    #     if len(res[j]) == maxIntLength:
    #         print(res[j], end='')
    #         break
    # print(',' + str(maxIntLength))
    return maxInt


if __name__ == "__main__":
    line = input()
    print(findMaxIntString(line))

# line = input()
# findMaxIntString(line)