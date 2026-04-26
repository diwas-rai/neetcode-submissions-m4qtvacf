# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not p and not q:
                return True
            elif not p and q or not q and p:
                return False
            elif p.val != q.val:
                return False

            return isSame(p.left, q.left) and isSame(p.right, q.right)
        
        stk = [root]

        while stk:
            node = stk.pop()

            if node:
                if isSame(node, subRoot):
                    return True
                stk.append(node.left)
                stk.append(node.right)
        
        return False
    