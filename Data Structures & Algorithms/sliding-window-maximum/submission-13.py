class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = 0
        res = []
        
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
        
            if q and q[0] < l:
                q.popleft()
            
            if r >= k - 1:
                res.append(nums[q[0]])
                l += 1

        return res
