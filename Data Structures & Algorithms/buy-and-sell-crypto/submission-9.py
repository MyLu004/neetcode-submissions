class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxVal = 0
        for i in range(len(prices)-1):
            j = i+1
            while j <= len(prices) - 1:
                maxVal = max(maxVal, prices[j] - prices[i])
                j+=1

    
        return maxVal