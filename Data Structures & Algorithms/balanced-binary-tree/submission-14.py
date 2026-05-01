# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stk = [root]
        processed = {None: 0} # Node : height

        while stk:
            node = stk[-1]

            if node:
                if node.left and node.left not in processed:
                    stk.append(node.left)
                elif node.right and node.right not in processed:
                    stk.append(node.right)
                else:
                    node = stk.pop()
                    left_h = processed[node.left]
                    right_h = processed[node.right]
                    if abs(left_h - right_h) > 1:
                        return False
                    processed[node] = max(left_h, right_h) + 1
    
        return True