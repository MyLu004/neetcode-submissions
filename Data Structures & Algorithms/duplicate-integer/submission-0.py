class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        result = False
        for i in nums:
            if i in mySet:
                result = True
            else:
                mySet.add(i)
        return result
        