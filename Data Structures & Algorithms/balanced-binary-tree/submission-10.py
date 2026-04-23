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
        node_to_height = {None: 0}

        while stk:
            node = stk[-1]

            if node.left and node.left not in node_to_height:
                stk.append(node.left)
            elif node.right and node.right not in node_to_height:
                stk.append(node.right)
            else:
                node = stk.pop()
                node_to_height[node] = 1 + max(node_to_height[node.left], node_to_height[node.right])

                if abs(node_to_height[node.left] - node_to_height[node.right]) > 1:
                    return False

        return True