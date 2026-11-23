class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #myList = [i+1 for i in range(max(piles))]

        left = 1
        right = max(piles)
        
        res = right

        while left <= right:
            hour = 0
            mid = (left+right) // 2
        
            for i in piles: #T O(n)
                #print("cal:",math.ceil(i / mid))
                hour = hour + math.ceil(i / mid)
                
            if hour <= h:
                res = min(res, mid)
                right = mid - 1
            
            elif hour > h:
                left = mid + 1
            
            #res = min(mid, h)
        
        return res
            
            