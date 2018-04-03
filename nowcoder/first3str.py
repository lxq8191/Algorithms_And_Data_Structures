# coding=utf-8
# 求一个字符串中第一个出现3次的字符。
def first3str(ss):
    dic = {}
    for i in range(len(ss)):
        if ss[i] in dic.keys():
            if dic[ss[i]] == 2:
                return ss[i]
            else:
                dic[ss[i]] += 1
        else:
            dic[ss[i]] = 1
    return -1


res = first3str('asdfass')
print(res)