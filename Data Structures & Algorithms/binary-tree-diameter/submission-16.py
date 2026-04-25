# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stk = [root]
        processed = {None: (0, 0)} # node : (height, diameter)

        while stk:
            node = stk[-1] 

            if node.left and node.left not in processed:
                stk.append(node.left)
            elif node.right and node.right not in processed:
                stk.append(node.right)
            else:
                node = stk.pop()

                left_h, left_d = processed[node.left]
                right_h, right_d = processed[node.right]
                processed[node] = (1 + max(left_h, right_h), max(left_h + right_h, left_d, right_d))
            
        return processed[root][1]