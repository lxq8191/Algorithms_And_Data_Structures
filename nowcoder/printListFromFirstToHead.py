# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        temp = []
        if listNode==None:
            return temp
        while listNode is not None:
            temp.append(listNode.val)
            listNode = listNode.next
        temp.reverse()
        return temp