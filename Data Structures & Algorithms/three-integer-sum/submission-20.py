class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            a = nums[i]

            if a > 0:
                break

            if i > 0 and a == nums[i-1]:
                continue
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                summ = a + nums[j] + nums[k]

                if summ > 0:
                    k -= 1
                elif summ < 0:
                    j += 1
                else:
                    res.append([a, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
            
        return res
