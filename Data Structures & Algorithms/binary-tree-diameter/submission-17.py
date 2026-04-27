# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stk = [root]
        processed = {None : (0, 0)} # node : (h, d)

        while stk:
            node = stk[-1]

            if node.left and node.left not in processed:
                stk.append(node.left)
            elif node.right and node.right not in processed:
                stk.append(node.right)
            else:
                node = stk.pop()

                h = 1 + max(processed[node.left][0], processed[node.right][0])
                d = max(processed[node.left][0] + processed[node.right][0], processed[node.left][1], processed[node.right][1])

                processed[node] = (h, d)
        
        return processed[root][1]