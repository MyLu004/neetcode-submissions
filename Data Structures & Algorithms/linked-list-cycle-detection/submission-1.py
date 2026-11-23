# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #start slow and fast at the same position
        slow, fast = head,head

        while fast and fast.next: #cause fast will reach null first before slow
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
            
        return False
         
