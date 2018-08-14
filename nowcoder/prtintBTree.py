# -*- coding:utf-8 -*-

# 按层打印二叉树，每层一个数组。
# 如果不分每层一个数组的话，去掉last和nlast变量即可。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreePrinter:
    def printTree(self, root):
        # write code here
        if not root:
            return []
        queue = []
        result = []
        last = nlast = root
        queue.append(root)
        cur_level = []
        while len(queue) > 0:
            node = queue.pop(0)
            cur_level.append(node.val)
            if node.left:
                queue.append(node.left)
                nlast = node.left
            if node.right:
                queue.append(node.right)
                nlast = node.right
            if node == last:
                result.append(cur_level)
                cur_level = []
                last = nlast
        return result
