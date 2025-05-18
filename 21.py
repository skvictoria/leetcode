# '''
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.
# '''

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         result = ListNode()
#         temp = result
#         while(list1 and list2):
#             if(list1.val <= list2.val):
#                 # append list1
#                 temp.next = list1
#                 list1 = list1.next
#                 temp = temp.next
#             elif(list1.val > list2.val):
#                 # append list2
#                 temp.next = list2
#                 list2 = list2.next
#                 temp = temp.next
#         if(list1 or list2):
#             if not list1 and not list2:
#                 return result
#             elif not list1:
#                 # append list2
#                 temp.next = list2
#             elif not list2:
#                 # append list1
#                 temp.next = list1
#         else:
#             temp = None
        
#         return result.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        
        result = ListNode()
        temp = ListNode()
        temp = result
        
        while list1 is not None and list2 is not None:
            if list1.val >= list2.val:
                tmpNode = ListNode()
                tmpNode.val = list2.val
                tmpNode.next = list2.next
                temp.next = tmpNode
                #temp.next = list2
                list2 = list2.next
            elif list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            temp = temp.next
        
        if list1 is not None:
            temp.next = list1
        if list2 is not None:
            temp.next = list2
        
        return result.next
    
sol = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
print(sol.mergeTwoLists(list1,list2).val)