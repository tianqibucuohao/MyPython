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
    def preorderTraversal(self, root: TreeNode) -> List[int]:  
        pass