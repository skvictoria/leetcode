# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = head
        length = 1
        if head is None:
            return None

        while head.next is not None:
            length += 1
            if length % 2 == 0:
                mid = mid.next
            head = head.next

        return mid