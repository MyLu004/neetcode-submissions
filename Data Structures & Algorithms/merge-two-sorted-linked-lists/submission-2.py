# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #take care the edge case: inserting into the empty list
        tail = dummy

        while list1 and list2: #while both are non empty
            if list1.val < list2.val:
                tail.next = list1
                list1 =  list1.next #update l1 pointer
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1: 
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next