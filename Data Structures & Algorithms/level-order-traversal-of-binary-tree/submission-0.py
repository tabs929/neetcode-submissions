# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        ans = []

        while q:
            lvl = []
            lenq = len(q)
            for i in range(lenq):
                curr = q.popleft()
                if curr:
                    lvl.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if lvl:
                ans.append(lvl)

        return ans