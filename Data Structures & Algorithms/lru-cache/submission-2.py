class Node:
    def __init__(self,key, val):
        self.key = key
        self.val = val
        
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.myList = {} #map key to node

        #dummy node for LRU and MRU
        self.left = Node(0,0)
        self.right = Node(0,0)

        #initial the connect between these 2 nodes
        self.left.next = self.right
        self.right.prev = self.left

    
    #HELP FUNCTION for the linked list

    #remove node from list 
    def remove(self,node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
    
    #insert node at right most
    def insert(self,node):
        prev = self.right.prev
        nxt =self.right

        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev


    def get(self, key: int) -> int: 
        #update the most recent everytime we do get value
        if key in self.myList:
            self.remove(self.myList[key])
            self.insert(self.myList[key])
            return self.myList[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.myList:
            self.remove(self.myList[key])
        
        self.myList[key] = Node(key,value)
        self.insert(self.myList[key])

        #remove the node if the list exceed the capacity
        #remove from the list and delte the LRU from the hashmap
        if len(self.myList) > self.capacity:
            lru = self.left.next 
            self.remove(lru)
            del self.myList[lru.key] 
        
