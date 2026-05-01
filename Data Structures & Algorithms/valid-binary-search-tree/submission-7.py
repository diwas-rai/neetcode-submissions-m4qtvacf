# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stk = [[root, [float('-inf'), float('inf')]]] # node : bounds

        while stk:
            node, bounds = stk.pop()

            if node:
                if node.val > bounds[1]:
                    return False
                elif node.val < bounds[0]:
                    return False

                lb = max(node.val + 1, bounds[0])
                ub = min(node.val - 1, bounds[1])
                stk.append([node.left, [bounds[0], ub]])
                stk.append([node.right, [lb, bounds[1]]])

        return True
                
