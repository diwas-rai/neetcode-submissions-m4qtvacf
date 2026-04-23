class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        []
        # 121 -> [0] -> [2] -> [2, 1]
        # 210 -> [2, 1] -> [2, 1, 0]
        # 101 -> [1, 1]

        q = deque()
        l = 0
        res = []
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if q and q[0] < l:
                q.popleft()
            
            if r - l + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        
        return res