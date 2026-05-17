/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
       // Points to next node in the list, next node of type
       // ListNode* - can't be passed by value (inf size)
 *     ListNode *next; // Holds mem address of following node

       // Three overloaded constructors - used dep on initial information

       // Def constructor - no args, 0 val node with no next node (dummy)
 *     ListNode() : val(0), next(nullptr) {}
       // One arg - Creates node with no follow up
 *     ListNode(int x) : val(x), next(nullptr) {}
       // Two arg - Node and known follow up
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
        // If the head points to the next and not nullptr
        if (head->next) {
            // Set newHead to recursive call to function with the head
            // parameter being the head which points to next
            newHead = reverseList(head->next);
            // Set current head to the one after next
            head->next->next = head;
        }
        // else, list ends, set to nullptr
        head->next = nullptr;

        // Recursive return of the newHead (Not too sure)
        return newHead;
    }
};
