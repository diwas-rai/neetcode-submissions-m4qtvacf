class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> groups;

        for (std::string& s : strs) {
            std::string key = s;
            std::ranges::sort(key);
            // Move into the map to avoid deep-copying s if strs is consumed
            groups[std::move(key)].push_back(std::move(s));
        }

        std::vector<std::vector<std::string>> res;
        res.reserve(groups.size());

        for (auto& [_, group] : groups) {
            res.push_back(std::move(group));
        }

        return res;
    }
};
