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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* right{head};

        while (n > 0)
        {
            --n;
            right = right->next;
        }

        ListNode dummy{0, head};
        ListNode* curr{&dummy};

        while (right)
        {
            curr = curr->next;
            right = right->next;
        }
        curr->next = curr->next->next;

        return dummy.next;
    }
};
