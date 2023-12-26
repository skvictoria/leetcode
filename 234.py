# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tailList = []
        while(head != None):
            tailList.append(head.val)
            head = head.next
        
        half_len = len(tailList)/2
        
        for i in range(int(half_len)):
            if(tailList[i] != tailList[len(tailList)-i-1]):
                return False

        return True

def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

gg = Solution()
gg.isPalindrome(create_linked_list([1,2,2,1]))