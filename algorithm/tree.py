# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:30:41 2019

@author: Administrator

tree遍历方式：
pre-order ：前序:父节点->左节点->右节点
in-order：中序：左节点->父节点->右节点
post-order:后序：左节点->右节点->父节点

"""

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.lef = None
        self.right = None
        
class Solution:
    def __init__(self,root = None):
        self.preorder = []
        self.inorder = []
        self.postorder = []
        self.deepth = 0
        self.root = root

    def preorderTraversal(self, root: TreeNode) -> list[int]:  
        if (root):
            self.preorder.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.preorder
    
    def inorderTraversal(self, root:TreeNode) -> list[int]:
        if (root):
            self.inorderTraversal(root.left)
            self.inorder.append(root.val)
            self.inorderTraversal(root.right)
        return self.inorder
    def postorderTraversal(self,root:TreeNode) -> list[int]:
        if (root):
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.postorder.append(root.val)
        return self.postorder
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if (not root):
            return []
        q=[root]
        res=[]
        while(q):
            templist = []
            length = len(q)
            for i in range(length):
                temp = q.pop(0)
                templist.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            res.append(templist)
        return res[::]
    def maxDepth(self, root:TreeNode) -> int:
        if (not root):
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
    
    def cmp(self, left:TreeNode, right:TreeNode) ->bool:
        if (left == None and right == None):
            return True
        if (left and right and left.val == right.val):
            return self.cmp(left.left, right.right) and self.cmp(left.right, right.left)
        return False
    def isSymmetric(self, root: TreeNode) -> bool:
        if (root):
            return self.cmp(root.left,root.right)
        return True