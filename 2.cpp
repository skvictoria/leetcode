
class ListNode
{
public:
    int val;
    ListNode* next;
    ListNode()
    {
        val = 0;
        next = nullptr;
    }
    ListNode(int x)
    {
        val = x;
        next = nullptr;
    }
    ListNode(int x, ListNode* next)
    {
        val = x;
        next = next;
    }
};

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        ListNode* output = new ListNode(0);
        ListNode* outputnode = output;
        bool bContinue = true;
        int temp;
        while(bContinue == true)
        {
            ListNode* nextnode = new ListNode();
            outputnode->val += (l1->val + l2->val);
            temp = outputnode->val;
            outputnode->val = temp % 10;
            
            nextnode->val = temp / 10;
            
            // if l1 and l2 are both not finished,
            if((l1->next != nullptr) && (l2->next != nullptr))
            {
                l1 = l1->next;
                l2 = l2->next;
            }
            // if l1 is not finished and l2 is finished,
            else if((l1->next != nullptr) && (l2->next == nullptr))
            {
                l1 = l1->next;
                l2->val = 0;
            }
            // if l1 is finished and l2 is not finished,
            else if((l1->next == nullptr) && (l2->next != nullptr))
            {
                l2 = l2->next;
                l1->val = 0;
            }
            else if(nextnode->val != 0)
            {
                l1->val = 0;
                l2->val = 0;
            }
            else
            {
                bContinue = false;
            }
            if(bContinue == true)
            {
                outputnode->next = nextnode;
                outputnode = outputnode->next;
            }
        }
        return output;
    }
};

int main()
{
    Solution sol;
    ListNode* next = new ListNode(9);
    ListNode* a = new ListNode(9,next);
    ListNode* b = new ListNode(9);
    sol.addTwoNumbers(a, b);
    return 0;
}