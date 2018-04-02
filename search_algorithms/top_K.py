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

# 使用heapq实现小顶堆
ans = []
heapq.heappush(ans,3) # 加入堆
heapq.heappop(ans)

# 如果想要实现大顶堆，在加入堆中时取其相反数，取出时再取其相反数即可
ans = []
heapq.heappush(ans,-3) # 加入堆
heapq.heappop(ans)

# 将列表调整成小顶堆
lst = [1,5,3,7,9]
heapq.heapify(lst)

