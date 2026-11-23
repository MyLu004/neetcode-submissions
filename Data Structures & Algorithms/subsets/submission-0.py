class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return # return nothing
            subset.append(nums[i])
            dfs(i+1) # do the depth search to add the subset if still need
            subset.pop() # if not, BACKTRACKING HERE
            dfs(i+1) # checking the second elememt to do the backtracking

        dfs(0)

        return res

            
