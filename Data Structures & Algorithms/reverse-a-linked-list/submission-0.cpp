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
    ListNode* reverseList(ListNode* head) {
        // Empty head
        if (!head) {
            return nullptr;
        }

        // Head not empty
        // Create newHead of struct* type, set it to current head
        ListNode* newHead = head;
        // If the head points to the next 
        if (head->next) {
            // Set newHead to recursive call to function with the head
            // parameter being the head which points to next
            newHead = reverseList(head->next);
            // Unsure what this means - come back to it later
            head->next->next = head;
        }
        // else set to nullptr
        head->next = nullptr;

        // Recursive return of the newHead (Not too sure)
        return newHead;
    }
};
