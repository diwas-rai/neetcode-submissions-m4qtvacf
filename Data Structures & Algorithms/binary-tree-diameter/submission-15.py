# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stk = [root]
        processed_nodes = {None: (0, 0)} # node : (height, diameter)
        while stk:
            node = stk[-1]

            if node.left and node.left not in processed_nodes:
                stk.append(node.left)
            elif node.right and node.right not in processed_nodes:
                stk.append(node.right)
            else:
                node = stk.pop()

                left_height, left_diameter = processed_nodes[node.left]
                right_height, right_diameter = processed_nodes[node.right]

                processed_nodes[node] = (1 + max(left_height, right_height), 
                                        max(left_height + right_height, left_diameter, right_diameter))
                left_height, left_diameter = processed_nodes[node.left]
                left_height, left_diameter = processed_nodes[node.left]
            
        return processed_nodes[root][1]