class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
        {
            return false;
        }

        std::map<char, int> s_count{};
        std::map<char, int> t_count{};

        for (size_t i{0}; i < s.length(); ++i)
        {
            s_count[s[i]]++;
            t_count[t[i]]++;
        }

        return s_count == t_count;
    }
};
