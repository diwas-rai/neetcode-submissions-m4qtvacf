class Solution {
public:

    string encode(vector<string>& strs) {
        string res{};
        for (const auto& s : strs)
        {
            res += to_string(s.size()) + '#' + s;
        }

        return res;
    }

    vector<string> decode(string s) {
        vector<string> res{};
        int l{0};
        int r{0};

        
        while (r < s.size())
        {
            while (r < s.size() && s[r] != '#')
            {
                ++r;
            }

            int word_len = stoi(s.substr(l, r - l));
            l = r + 1;
            r = l + word_len;

            res.push_back(s.substr(l, r - l));
            l = r;
        }

        return res;
    }
};
