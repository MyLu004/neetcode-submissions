class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # time complexity : O(n*m)
        
        # using max heap - negate the value
        # using queue and hashmap to keep track of time count for n time
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0 
        q = deque() # pairs of [-cnt, idleTime]
        
        # while maxHeap not empty
        # OR queue is not empty
        while maxHeap or q:
            time += 1

            if maxHeap: #if maxHeap is not empty
                cnt = 1 + heapq.heappop(maxHeap)

                if cnt:
                    q.append([cnt, time+n])
            
            if q and q[0][1] == time: #if queue is not empty
                heapq.heappush(maxHeap,q.popleft()[0])
        
        return time


