# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        #find the middle point of the list
        while fast and fast.next: #while fast not reach the end yet
            slow = slow.next #jump 1 time
            fast = fast.next.next #jump 2 times

        #second half of list : GOAL : reverse the second half of the list
        second = slow.next
        prev = slow.next = None

        while second:
            temp_var = second.next
            second.next = prev
            prev = second
            second = temp_var
        
        #merge two half of the list
        first, second = head, prev
        
        while second: #while second is not null
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1

            first,second = tmp1,tmp2
        

