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
        max_heap = []

        for i in range(len(nums)):
            heapq.heappush(max_heap, [-nums[i], i])

            if i >= k - 1:
                while max_heap[0][1] <= i - k:
                    heapq.heappop(max_heap)
                res.append(-max_heap[0][0])

        return res