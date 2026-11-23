class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # conver the array into the negative for max heap = -(min_heap)
        heapq.heapify(stones)
        print("my list: ", stones)
        while len(stones)>1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            curr = first - second
            if curr == 0:
                pass
            else:
                heapq.heappush(stones, curr)
            
        stones.append(0)

        return abs(stones[0])
                