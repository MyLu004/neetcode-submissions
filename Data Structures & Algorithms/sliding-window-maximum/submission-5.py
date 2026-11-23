class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        if len(nums) == 1:
            return nums
        for i in range(len(nums)-k+1):
            myVal  = max(list(i for i in nums[i:i+k]))
            result.append(myVal)
    
        return result
       