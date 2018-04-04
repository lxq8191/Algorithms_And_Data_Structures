# -*- coding:utf-8 -*-
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