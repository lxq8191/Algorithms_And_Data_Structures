import Queue
import heapq

class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''
    def topk(self, nums, k):
        # Write your code here
        res = []
        if not nums or k == 0:
            return res
            
        MaxHeap = Queue.PriorityQueue()
        for num in nums:
            MaxHeap.put(-num)
        
        for i in range(k):
            res.append(-MaxHeap.get())
        
        return res

sl = Solution()
nums = [4,2,8,1,9]
print(sl.topk(nums, 3))

print(heapq.nlargest(3, nums)) # top K大的数字
print(heapq.nsmallest(3, nums)) # 最小的K个数字