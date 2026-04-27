# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stk = [root]

        while stk:
            node = stk.pop()

            if not node:
                continue

            if node.val >= p.val and node.val <= q.val:
                return node
            elif node.val >= q.val and node.val <= p.val:
                return node
        
            stk.append(node.left)
            stk.append(node.right)