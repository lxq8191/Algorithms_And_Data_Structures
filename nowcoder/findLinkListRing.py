# coding=utf-8
# 查找单链表中是否存在
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
            
    # 定义两个指针，一个快指针，一个慢指针，当两个指针重合时说明有环
    def findRingNode(self, p):
        if p == None:
            return None
        pSlow = p.next
        if pSlow == None:
            return None
        pFast = pSlow.next
        while pSlow != None and pFast != None:
            if pSlow == pFast:
                return pFast
            pSlow = pSlow.next
            pFast = pFast.next
            if pFast != None:
                pFast = pFast.next
        return None

