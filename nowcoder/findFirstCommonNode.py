# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        len1 = self.GetListLength(pHead1)
        len2 = self.GetListLength(pHead2)
        pLone = pHead1
        pShort = pHead2
        if len1 < len2:
            pLone = pHead2
            pShort = pHead1
        for i in range(abs(len1 - len2)):
            pLone = pLone.next
        while pLone != pShort and pLone!=None and pShort!=None:
            pLone = pLone.next
            pShort = pShort.next
        return pLone
    def GetListLength(self, p):
        pLen = 0
        while p!=None:
            pLen += 1
            p = p.next
        return pLen