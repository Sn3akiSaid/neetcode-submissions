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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (!list1) { return list2; }
        if (!list2) { return list1; }
        // Head of first list <= to head of 2nd list
        if (list1->val <= list2->val) {
            // Set the next pointer of list1 to merged result of remaining nodes
            list1->next = mergeTwoLists(list1->next, list2);
            // Return list1 as current head
            return list1;
        }
        else {
            // Set the next pointer of list2 to merged result of reminaing nodes
            list2->next = mergeTwoLists(list1, list2->next);
            // Return list2 as current head
            return list2;
        }
        


    }
};
