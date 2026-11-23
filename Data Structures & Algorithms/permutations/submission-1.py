class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: #base case, return the array
            return [[]]

        perms = self. permute(nums[1:]) #get rid the rotation from everything except the first one

        res = []

        for p in perms:
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i,nums[0])
                
                #append the list to the result
                res.append(p_copy)


        return res