class MedianFinder:

    def __init__(self):

        #idea: need to be approximate equal

        self.SmallHeap = []
        self.LargeHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.SmallHeap, -num) #negate the value for the min heap

        #make sure every num small is <= every num in large
        if (self.SmallHeap and self.LargeHeap and (-self.SmallHeap[0] > self.LargeHeap[0])):
            val = -1 * heapq.heappop(self.SmallHeap)
            heapq.heappush(self.LargeHeap, val)
            
        # uneven size? need to bounde to balance between 2 lists
        if (len(self.SmallHeap) > len(self.LargeHeap)+1):
            val = -1 * heapq.heappop(self.SmallHeap)
            heapq.heappush(self.LargeHeap, val)

        if (len(self.LargeHeap) > len(self.SmallHeap)):
            val = heapq.heappop(self.LargeHeap)
            heapq.heappush(self.SmallHeap, -val)



    def findMedian(self) -> float:
        heapq.heapify(self.LargeHeap)
        
        #odd len
        if (len(self.SmallHeap) > len(self.LargeHeap)): 
            return -self.SmallHeap[0]
        
        if (len(self.SmallHeap) < len(self.LargeHeap)):
            return self.LargeHeap[0]
        
        #else
        return (-self.SmallHeap[0] + self.LargeHeap[0])/2


            
