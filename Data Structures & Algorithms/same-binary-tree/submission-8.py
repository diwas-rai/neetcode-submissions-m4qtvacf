# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_stk= [p]
        q_stk = [q]

        while p_stk and q_stk:
            p_node = p_stk.pop()
            q_node = q_stk.pop()

            if (not p_node and q_node) or (not q_node and p_node):
                return False
            
            if p_node and q_node:
                if p_node.val != q_node.val:
                    return False
                
                p_stk.append(p_node.right)
                p_stk.append(p_node.left)
                q_stk.append(q_node.right)
                q_stk.append(q_node.left)
        
        return q_stk == p_stk