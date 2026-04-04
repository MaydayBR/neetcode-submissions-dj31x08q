# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root, path, val):
            if not root:
                return None
            path.append(root)
            if root == val or root.val == val or root.val == val.val:
                return path[:]
                
            left = dfs(root.left, path, val)
            if left:
                return left
            right = dfs(root.right, path, val)
            if right:
                return right
            
            path.pop()
            return None

        p_trail = dfs(root,[],p)
        q_trail = set(dfs(root,[],q))
        for i in range(len(p_trail)-1,-1,-1):
            if p_trail[i] in q_trail:
                return p_trail[i]
        
        return None
        








