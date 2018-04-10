# -*- coding:utf-8 -*-
# 1到n之间1出现的次数
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1,n+1):
            while(i!=0):
                yushu = i % 10
                if(yushu==1):
                    count += 1
                i = int(i / 10)
        return count