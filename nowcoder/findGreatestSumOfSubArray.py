# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        dp = [array[0]]
        i = 1
        for num in array[1:]:
            if dp[i - 1] <= 0:#之前小于等于零的和舍弃掉
                dp.append(num)
            else:#之前大于零的和继续加上当前这个数
                dp.append(dp[i - 1] + num)
            i += 1
        return max(dp)#返回dp中最大值，即最大连续子数组和