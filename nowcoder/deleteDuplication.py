# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead==None or pHead.next==None:
            return pHead
        pNewHead = pHead
        pPreNode = None
        pNode = pHead
        while pNode!=None:
            pNext = pNode.next
            deleteFlag = False
            if pNext!=None and pNode.val == pNext.val:
                deleteFlag = True
            if not deleteFlag:
                pPreNode = pNode
                pNode = pNode.next
            else:
                value = pNode.val
                pDel = pNode
                while pDel!=None and pDel.val == value:
                    pNext = pDel.next
                    pDel = pNext
                if pPreNode==None:
                    pNewHead = pNext
                else:
                    pPreNode.next = pNext
                pNode = pNext
        return pNewHead