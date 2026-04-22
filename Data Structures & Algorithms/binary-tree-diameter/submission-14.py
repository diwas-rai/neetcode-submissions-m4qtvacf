# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stk = [root]
        mp = {None: (0, 0)}

        while stk:
            node = stk[-1]

            if node.left and node.left not in mp:
                stk.append(node.left)
            elif node.right and node.right not in mp:
                stk.append(node.right)
            else:
                node = stk.pop()
                
                left_height, left_diameter = mp[node.left]
                right_height, right_diameter = mp[node.right]

                mp[node] = (1 + max(left_height, right_height), max(left_height + right_height, left_diameter, right_diameter))

        return mp[root][1]