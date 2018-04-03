# coding=utf-8
class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # 注意下标变化 
        dc = 0 
        for i in range(len(A)):
            if A[i-dc] == elem:
                A.remove(elem)
                dc = dc + 1
        return A

sl = Solution()
A = [1,2,3,5,5,6,7]
elem = 5
print(sl.removeElement(A, elem))