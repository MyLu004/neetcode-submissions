class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negList = [-x for x in nums]
        heapq.heapify(negList)

        for i in range(k):
            result = heapq.heappop(negList)
        
        return -result