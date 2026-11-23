# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr: #while currect not None
            nxt = curr.next #save the data before broke the link
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        
        