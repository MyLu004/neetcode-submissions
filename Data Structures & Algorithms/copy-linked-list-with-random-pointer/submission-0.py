"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None : None}
        curr = head
        
        #FIRST PASS: clone the linked list and map to the hash
        while curr:
            #old = curr
            copy = Node(curr.val)

            #map the old node to the copy we just make
            oldToCopy[curr] = copy

            #update the curr pointer until it reach to the end
            curr = curr.next
        
        curr = head
        #SECOND PASS: link the pointer
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]


