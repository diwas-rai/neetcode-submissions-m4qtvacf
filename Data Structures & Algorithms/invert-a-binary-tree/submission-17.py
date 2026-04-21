# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stk = [root]

        while stk:
            curr = stk.pop()
            if curr:
                stk.append(curr.left)
                stk.append(curr.right)
                curr.left, curr.right = curr.right, curr.left
        
        return root