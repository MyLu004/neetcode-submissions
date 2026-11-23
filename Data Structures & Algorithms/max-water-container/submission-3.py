class Solution:
    def maxArea(self, heights: List[int]) -> int:

        sumArea = 0
        l,r = 0, len(heights)-1
        while l < r:
            sumArea = max(sumArea,(min(heights[l], heights[r]) * (r-l)))
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] <= heights[r]:
                l += 1

        return sumArea