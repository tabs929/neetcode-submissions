class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSum = float("-inf")

        def dfs(node):
            if not node:
                return 0
            
            leftSum = max(0,dfs(node.left))
            rightSum = max(0,dfs(node.right))
            self.maxPathSum = max(self.maxPathSum, node.val+leftSum+rightSum)
            return max(leftSum,rightSum)+node.val
        
        dfs(root)
        return self.maxPathSum