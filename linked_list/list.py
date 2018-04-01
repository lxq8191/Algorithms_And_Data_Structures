# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        ringNode = self.FindRing(pHead)
        if ringNode==None:
            return None
        ringLen = 1
        pNext = ringNode.next
        while pNext != ringNode:
            ringLen += 1
            pNext = pNext.next
        pAhead = pHead
        pTail = pHead
        for i in range(ringLen):
            pAhead = pAhead.next
        while pAhead!=None and pTail!=None:
            if pAhead==pTail:
                return pAhead
            pAhead = pAhead.next
            pTail = pTail.next
        return pAhead
            
    def FindRing(self, p):
        if p == None:
            return None
        pSlow = p.next
        if pSlow == None:
            return None
        pFast = pSlow.next
        while pSlow!=None and pFast!=None:
            if pSlow == pFast:
                return pFast
            pSlow = pSlow.next
            pFast = pFast.next
            if pFast != None:
                pFast = pFast.next
        return None

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