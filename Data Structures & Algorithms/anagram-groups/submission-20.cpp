class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, int> idx; // sorted key -> group idx
        vector<vector<string>> res;

        for (const string& s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            
            auto [it, inserted] = idx.try_emplace(key, res.size());

            if (inserted) res.emplace_back();

            res[it->second].push_back(s);
        }

        return res;
    }
};
