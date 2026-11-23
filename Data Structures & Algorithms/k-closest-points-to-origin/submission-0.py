class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        myList = []

        for x, y in points:
            distance = x**2 + y**2
            myList.append([distance, x,y])
        

        heapq.heapify(myList)
        res = []

        while k > 0:
            distance, x, y = heapq.heappop(myList)
            res.append([x,y])
            k -= 1
        return res

        