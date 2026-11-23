class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # idea: compute the subset, then compute the sum and keep that equal to the target
        res = []

        def dfs(i, cur, total):
            if (total == target): #found the combination
                res.append(cur.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            nums[i]
 
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0,[],0)

        return res
            
       