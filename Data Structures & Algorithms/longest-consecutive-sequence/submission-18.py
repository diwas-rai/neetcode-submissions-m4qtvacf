class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in nums:
            if num - 1 not in num_set:
                curr_len = 1
                while num + curr_len in num_set:
                    curr_len += 1
                longest = max(curr_len, longest)
        return longest