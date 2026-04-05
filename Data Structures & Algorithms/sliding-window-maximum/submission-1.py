"""
array of ints: nums
int: k
sliding window of size k
window slides until right edge of arr
return list containing max element in window at each step
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
            
        for r in range(len(nums)):
            if (r - l + 1) == k:
                res.append(max(nums[l:r+1]))
                l += 1

        return res