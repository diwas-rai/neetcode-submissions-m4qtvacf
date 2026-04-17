class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if a > 0:
                break
                
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                b, c = nums[l], nums[r]
                three_sum = a + b + c

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a,b,c])
                    l += 1

                    while l < r and nums[l-1] == nums[l]:
                        l += 1

        return res