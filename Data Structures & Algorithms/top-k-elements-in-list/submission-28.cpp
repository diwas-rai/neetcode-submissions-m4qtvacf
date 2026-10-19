class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count{};

        for (const auto& num : nums) 
        {
            ++count[num];
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, std::greater<pair<int, int>>> min_heap{};

        for (const auto& [num, freq] : count)
        {
            min_heap.emplace(freq, num);

            if (min_heap.size() > k)
            {
                min_heap.pop();
            }
        }

        vector<int> result{};
        result.reserve(k);

        while (!min_heap.empty())
        {
            result.push_back(min_heap.top().second);
            min_heap.pop();
        }

        return result;
    }
};
