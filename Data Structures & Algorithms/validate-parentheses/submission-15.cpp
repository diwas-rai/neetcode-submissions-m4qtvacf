class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> mp {{']', '['}, {'}', '{'}, {')', '('}};
        std::stack<char> stk{};

        for (const auto& c : s)
        {
            if (mp.contains(c))
            {
                if (!stk.empty() && stk.top() == mp[c]) stk.pop();
                else return false;
            }
            else
            {
                stk.push(c);
            }
        }

        return stk.empty();
    }
};
