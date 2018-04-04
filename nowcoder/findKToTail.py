# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head==None or k == 0:
            return None
        listLen = self.GetListLength(head)
        if listLen < k:
            return None
        headNode = head
        tailNode = head
        for i in range(k - 1):
            tailNode = tailNode.next
        while tailNode.next!=None:
            headNode = headNode.next
            tailNode = tailNode.next
        return headNode
    def GetListLength(self, p):
        pLen = 0
        while p!=None:
            pLen += 1
            p = p.next
        return pLen