/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy = ListNode();
        ListNode* curr = &dummy;

        int carry{};
        while (l1 or l2 or carry)
        {
            int l1_val = l1 ? l1->val : 0;
            l1 = l1 ? l1->next : nullptr;
            int l2_val = l2 ? l2->val : 0;
            l2 = l2 ? l2->next : nullptr;
            
            int sum = l1_val + l2_val + carry;
            carry = 0;
            if (sum > 9) 
            {
                carry = sum / 10;
                sum %= 10;
            }

            curr->next = new ListNode(sum);
            curr = curr->next;
        }

        return dummy.next;
    }
};
