# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.helper(root,root.val)
        return self.ans

    def helper(self,node,m_val):
        if node:
            if node.val >= m_val:
                self.ans +=1
                m_val = node.val
            self.helper(node.left,m_val)
            self.helper(node.right,m_val)