# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
    
            right_h = dfs(node.right)
            if right_h == -1:
                return -1
    
            left_h = dfs(node.left)
            print(node.val, left_h)
            if left_h == -1:
                return -1
    
            if abs(left_h - right_h) > 1:
                return -1
    
            return 1 + max(left_h, right_h)
        
        return dfs(root) != -1