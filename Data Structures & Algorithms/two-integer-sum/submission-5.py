class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHashmap = {} # use hashmap for O(1) look up

        for i, val in enumerate(nums):
            diff = target - val
            if diff in myHashmap:
                return [myHashmap[diff],i]
            myHashmap[val] = i

        