# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # idea: last_sorted: tail of sorted node
        #       curr: node to insert into the sorted node
        dummy = ListNode()
        dummy.next = head
        last_sorted = head
        curr = head.next
        while curr:
            if last_sorted.val <= curr.val:
                last_sorted = curr
                curr = curr.next
            else:
                prev = dummy
                while prev.next and prev.next.val <= curr.val:
                    prev = prev.next
                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
                curr = last_sorted.next
        return dummy.next
            