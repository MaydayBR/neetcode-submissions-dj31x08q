# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum = float("-inf")
        def dfs(root):
            if not root:
                return float("-inf")
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.maximum = max(self.maximum , left , right , root.val ,left+root.val, right+root.val, root.val + left + right)
                
            return max(root.val, root.val + left , root.val + right)

        dfs(root)
        return self.maximum