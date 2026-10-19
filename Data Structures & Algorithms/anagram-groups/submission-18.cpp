class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string, vector<string>> groups{};

        for (const string& s : strs)
        {
            std::vector<int> chars(26);

            for (const char& c : s)
            {
                chars[c - 'a']++;
            }

            string key = to_string(chars[0]);
            for (int i = 1; i < 26; ++i) {
                key += ',' + to_string(chars[i]);
            }
            groups[key].push_back(s);
        }

        vector<vector<string>> res;
        for (const auto& [k, v] : groups)
        {
            res.push_back(v);
        }
        return res;
    }
};
