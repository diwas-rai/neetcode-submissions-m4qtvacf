# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = 0
        stk = [(root, 1)] 

        while stk:
            curr, curr_depth = stk.pop()

            if curr:
                stk.append((curr.left, curr_depth + 1))
                stk.append((curr.right, curr_depth + 1))

                max_depth = max(max_depth, curr_depth)
        
        return max_depth
