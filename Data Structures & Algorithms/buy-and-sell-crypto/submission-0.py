class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxVal = 0
        for index, value in enumerate(prices):
            if index == len(prices)-1 or value >= prices[index+1]:
                continue
            else:
                l = index
                r = len(prices)-1
                while l < r:
                    maxVal = max(maxVal, (prices[r]-prices[l]))
                    r -= 1
    
        return maxVal