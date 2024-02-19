'''
Algorithm: 
temp = head
while(temp.next is not None):
    1. stack.push(temp.val)
    2. temp = temp.next

result = []
while head.next is not None:
    result.append(stack[0])
    head = head.next

O(n*2)

Data structure:
head(input)
stack

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def makeList(self, elements):
        head = ListNode(elements[0])
        temp = head
        for i in range(1, len(elements)):
            temp.next = ListNode(elements[i])
            temp = temp.next
        return head
    
class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        if head is None:
            return None
        
        res = ListNode()
        temp = res
        stack = []
        
        while head:
            stack.append(head.val)
            head = head.next

        temp.val = stack.pop()
        while stack:
            temp.next = ListNode(stack.pop())
            temp = temp.next
        return res
    
Sol = Solution()
listnode = ListNode()
Sol.reverseList(listnode.makeList([1,2,3,4,5]))