# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stk = [[root, float('-inf')]] # [node, max val so far]
        res = 0

        while stk:
            node, max_val = stk.pop()

            if node:
                if node.val >= max_val:
                    max_val = node.val
                    res += 1
                
                stk.append([node.right, max_val])
                stk.append([node.left, max_val])
        
        return res