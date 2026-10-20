class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> stk;

        for (const auto& t : tokens)
        {
            if (t == "+")
            {
                int r = stk.top();
                stk.pop();
                int l = stk.top();
                stk.pop();
                stk.push(l + r);
            }
            else if (t == "-") {
                int r = stk.top();
                stk.pop();
                int l = stk.top();
                stk.pop();
                stk.push(l - r);
            }
            else if (t == "*") {
                int r = stk.top();
                stk.pop();
                int l = stk.top();
                stk.pop();
                stk.push(l * r);
            }
            else if (t == "/") {
                int r = stk.top();
                stk.pop();
                int l = stk.top();
                stk.pop();
                stk.push(l / r);
            }
            else {stk.push(stoi(t));}
        }

        return stk.top();
    }
};
