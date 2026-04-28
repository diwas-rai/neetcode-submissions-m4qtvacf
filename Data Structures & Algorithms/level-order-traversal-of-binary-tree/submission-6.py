# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([[root, 0]])
        mp = defaultdict(list) 

        while q:
            node, height = q.popleft()
            
            if node:
                mp[height].append(node.val)
                q.append([node.left, height + 1])
                q.append([node.right, height + 1])

        res = [[]] * len(mp)
        for k, v in mp.items():
            res[k] = v
        
        return res