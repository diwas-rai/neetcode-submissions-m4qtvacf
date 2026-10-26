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
    void reorderList(ListNode* head) {
        if (!head->next) { return; }
        ListNode* fast{head->next};
        ListNode* slow{head};

        while (fast && fast->next)
        {
            fast = fast->next->next;
            slow = slow->next;
        }

        ListNode* curr{slow->next};
        ListNode* prev{nullptr};
        slow->next = nullptr;
        while (curr)
        {
            ListNode* tmp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = tmp;
        }

        ListNode* h1 = head;
        ListNode* h2 = prev;
        while (h2)
        {
            ListNode* h1_tmp = h1->next;
            ListNode* h2_tmp = h2->next;
            h1->next = h2;
            h1 = h1_tmp;
            h2->next = h1;
            h2 = h2_tmp;
        }
    }
};
