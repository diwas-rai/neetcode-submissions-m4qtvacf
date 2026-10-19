class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen{};

        for (size_t i{0}; i < nums.size(); ++i)
        {
            int diff{target - nums[i]};

            if (seen.contains(diff))
            {
                return {seen[diff], static_cast<int>(i)};
            }

            seen[nums[i]] = i;
        }

        return {};
    }
};
