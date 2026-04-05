class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0

        for num in nums:
            if num - 1 not in nums_set:
                curr_length = 1
                while num + curr_length in nums_set:
                    curr_length += 1
                max_length = max(curr_length, max_length)
        
        return max_length