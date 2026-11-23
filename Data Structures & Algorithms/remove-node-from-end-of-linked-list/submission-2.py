# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head) #set data, and set as head
        left = dummy
        right = head #n+ 1 node

        while n > 0 and right: #and right is not null
            right = right.next
            n-=1
        
        while right:
            left = left.next
            right = right.next
        
        #delete
        left.next = left.next.next



        return dummy.next

        
        
